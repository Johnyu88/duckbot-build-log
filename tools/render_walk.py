"""不開視窗，直接在模擬裡跑 ONNX，輸出影片與位置數據。
用法（在 ~/Open_Duck_Playground）：
  MUJOCO_GL=egl uv run python render_walk.py -o <onnx路徑>
"""
import argparse
import numpy as np
import mujoco
from playground.open_duck_mini_v2.mujoco_infer import MjInfer, USE_MOTOR_SPEED_LIMITS

p = argparse.ArgumentParser()
p.add_argument("-o", "--onnx_model_path", required=True)
p.add_argument("--out", default="walk.mp4")
p.add_argument("--seconds", type=float, default=14.0)
p.add_argument("--scene", default="playground/open_duck_mini_v2/xmls/scene_flat_terrain.xml")
a = p.parse_args()

m = MjInfer(
    a.scene,
    "playground/open_duck_mini_v2/data/polynomial_coefficients.pkl",
    a.onnx_model_path,
    False,
)
cam = mujoco.MjvCamera()
cam.type = mujoco.mjtCamera.mjCAMERA_TRACKING
cam.trackbodyid = 1
cam.distance, cam.azimuth, cam.elevation = 0.7, 120, -15
r = mujoco.Renderer(m.model, height=480, width=640)

# 時間表：0-3 秒站著，3-8 秒前進，8-11 秒停，11-14 秒左轉
def cmd(t):
    if 3 <= t < 8:
        return [0.15, 0, 0]
    if t >= 11:
        return [0, 0, 1.0]
    return [0, 0, 0]

peak = np.zeros(m.model.nu)
frames, n_ctrl = [], int(a.seconds / (m.sim_dt * m.decimation))
for k in range(n_ctrl):
    t = k * m.sim_dt * m.decimation
    m.commands[0:3] = cmd(t)
    m.imitation_i = (m.imitation_i + 1.0) % m.PRM.nb_steps_in_period
    ph = m.imitation_i / m.PRM.nb_steps_in_period * 2 * np.pi
    m.imitation_phase = np.array([np.cos(ph), np.sin(ph)])
    obs = m.get_obs(m.data, m.commands)
    action = m.policy.infer(obs)
    m.last_last_last_action = m.last_last_action.copy()
    m.last_last_action = m.last_action.copy()
    m.last_action = action.copy()
    tg = m.default_actuator + action * m.action_scale
    if USE_MOTOR_SPEED_LIMITS:
        dt = m.sim_dt * m.decimation
        tg = np.clip(tg, m.prev_motor_targets - m.max_motor_velocity * dt,
                     m.prev_motor_targets + m.max_motor_velocity * dt)
        m.prev_motor_targets = tg.copy()
    m.motor_targets = tg
    m.data.ctrl = tg.copy()
    for _ in range(m.decimation):
        mujoco.mj_step(m.model, m.data)
        peak = np.maximum(peak, np.abs(m.data.actuator_force))
    if k % 2 == 0:
        r.update_scene(m.data, camera=cam)
        frames.append(r.render().copy())
    if k % 50 == 0:
        x, y, z = m.data.qpos[:3]
        print(f"t={t:5.1f}s  x={x:+.2f} y={y:+.2f} 高度z={z:.3f}")

try:
    import imageio
    imageio.mimsave(a.out, frames, fps=25)
except Exception as e:
    from PIL import Image
    a.out = a.out.replace(".mp4", ".gif")
    ims = [Image.fromarray(f) for f in frames]
    ims[0].save(a.out, save_all=True, append_images=ims[1:], duration=40, loop=0)
print("已輸出：", a.out)
print("\n各關節模擬中的最大力矩 (N·m；STS3215 7.4V 規格堵轉 1.91)：")
for i in range(m.model.nu):
    print(f"  {mujoco.mj_id2name(m.model, mujoco.mjtObj.mjOBJ_ACTUATOR, i):16s} {peak[i]:.2f}")
print("最大值：", round(float(peak.max()), 2))
