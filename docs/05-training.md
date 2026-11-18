# 05 訓練環境與流程

## 環境
Windows + WSL2 Ubuntu、RTX 4090 Laptop 16 GB、uv、Python 3.12。

## 安裝重點
    git clone https://github.com/Johnyu88/Open_Duck_Playground.git
    cd Open_Duck_Playground
    uv sync

原專案依賴沒有版本上限，新版本會壞。本 fork 已鎖定：
`jax[cuda12]<0.7`、`flax<0.11`、`brax<0.13`、`mujoco<3.4`、`mujoco-mjx<3.4`、`playground==0.0.5`。

## 訓練
    uv run playground/open_duck_mini_v2/runner.py --output_dir ~/duck_runs/test --num_timesteps 1000000

選項：`--output_dir`、`--num_timesteps`、`--env`、`--task`、`--restore_checkpoint_path`

## 監看（http://localhost:6006）
    uv run tensorboard --logdir=$HOME/duck_runs

## 模擬預覽
    uv run playground/open_duck_mini_v2/mujoco_infer.py -o $HOME/duck_runs/test/檔名.onnx

## 訓練紀錄
| 日期 | 步數 | 輸出目錄 | 最終 reward | 耗時 | 備註 |
|---|---|---|---|---|---|
| 2026-11-17 | 1M（實跑約 2.29M） | ~/duck_runs/test | ~24.9 | 約 4 分 | 首次測試 |

## Microduck 訓練（副線，模擬用）
Microduck 與 Open Duck Mini 是兩套互不相通的系統，策略不能互相轉用。這條線只在模擬裡驗證完整流程。

### 環境
`pollen-robotics/microduck_rl`，mjlab 1.3.0 + PPO（rsl_rl）、PyTorch、Python 3.12、uv。`uv sync` 後 `uv run list-envs` 列出 45 個任務。

### 指令
訓練（wandb 提示選 3 不使用，或先 `export WANDB_MODE=offline`）：

    cd ~/microduck_rl
    uv run train Mjlab-Velocity-Flat-MicroDuck --env.scene.num-envs 4096

接續訓練：

    uv run train Mjlab-Velocity-Flat-MicroDuck --env.scene.num-envs 4096 \
        --agent.run-name resume --agent.load-checkpoint model_XXXX.pt --agent.resume True

找最新 checkpoint（把 11-31-57 換成該次訓練的時間戳）：

    CKPT=$(find ~/microduck_rl/logs -path '*11-31-57*' -name 'model_*.pt' | sort -V | tail -1); echo $CKPT

匯出 ONNX（輸出 `output.onnx` 到目前資料夾）與模擬檢視：

    uv run scripts/export.py Mjlab-Velocity-Flat-MicroDuck --checkpoint-file "$CKPT"
    uv run play Mjlab-Velocity-Flat-MicroDuck --checkpoint-file "$CKPT"

WSL 的檢視視窗預設是軟體繪圖（實測 0.03 倍速、2 FPS）。啟用 GPU 繪圖後提升到約 0.53 倍速、26 FPS：

    export GALLIUM_DRIVER=d3d12
    export MESA_D3D12_DEFAULT_ADAPTER_NAME=NVIDIA

### 效能實測（RTX 4090 Laptop 16 GB）
| 環境數 | 每次迭代 | 顯存 | GPU 使用率 | 溫度／功耗 | 備註 |
|---|---|---|---|---|---|
| 1024 | 約 1.5 秒 | 約 3 GB | 28% | 72°C、68 W | 資源用不滿，不建議 |
| 4096 | 約 2.3–2.45 秒 | 約 7 GB | 57% | 86°C、108／119 W | 採用 |

這個任務的上限是 50,000 次迭代，每 250 次存一次 checkpoint。4096 環境完整跑完要超過一天，所以實際是中途停止。電腦長時間跑要注意散熱與電源（不要睡眠）。

### 訓練過程指標（4096 環境，看趨勢即可）
| 已訓練時間 | fell_over | error_vel_xy | error_vel_yaw | 備註 |
|---|---|---|---|---|
| 約 1 小時 | 0.375 | 0.43 | 1.26 | |
| 約 9 小時 | 0.25 | 0.41 | 0.94 | |
| 約 18 小時（停止時） | 0.21 | 0.42 | 0.88 | 進步已很慢 |

停止時 `time_out` 為 4.0，幾乎都撐到時間結束才重來；課程（Curriculum）已升到 `head_pose_range` 1.4、`standing_envs` 0.25。

### 訓練中的隨機化（讓策略耐用）
- 每 3–6 秒隨機推一下，速度變化最多 ±0.3 m/s
- 頭部、身體姿態指令每 2–5 秒重抽
- 每次重來：腳底摩擦 0.7–1.3 倍、關節摩擦、初始姿態重抽
- 每隻鴨子固定一次：質量與慣量 ±5%
- Flat 任務地面是平地，不換地形；粗糙地形另有 Rough 任務

### 目前狀態與未確認事項
- 已確認：checkpoint 載入、模擬檢視視窗開啟，小鴨在 2700 步以上沒有跌倒。
- **尚未確認：** 小鴨是否真的依速度指令往前走（靜態畫面看不出）；ONNX 匯出是否成功；`scripts/infer_policy.py --walking output.onnx` 的鍵盤操控。
- 專案說明提到的 `scripts/render_policy.py` 在這份程式碼裡不存在，不要用。

## 常見問題
| 症狀 | 原因 | 解法 |
|---|---|---|
| 指令回報 `路徑: No such file or directory` | 照貼了含 `<路徑>` 的佔位符，角括號被當成檔案轉向 | 換成真實路徑，不要保留角括號 |
| `navidia-smi` 找不到指令 | 拼錯 | 正確是 `nvidia-smi`，在 PowerShell 或 Ubuntu 都能跑 |
| 檢視視窗只有 2 FPS | WSL 軟體繪圖 | 設定 `GALLIUM_DRIVER=d3d12`（見上） |
| 訓練視窗 ETA 看起來太短 | 早期 ETA 估計不準，上限是 50,000 次迭代 | 以每次迭代時間乘以剩餘次數自行估算 |
| tensorflow 無 cp314 wheel | Python 3.14 太新 | `uv python pin 3.12` |
| cannot import name 'mjx' | mujoco 4.x 拆出 mjx | 改用鎖定版本 |
| device_put_replicated deprecated | JAX 與 brax 版本不合 | 降版本（見上） |
| TensorBoard No dashboards | 還沒寫出事件檔 | 稍後重新整理 |
| GPU OOM | 顯存不足 | `XLA_PYTHON_CLIENT_MEM_FRACTION=0.7` |
