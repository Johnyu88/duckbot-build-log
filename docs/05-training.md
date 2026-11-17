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

## 常見問題
| 症狀 | 原因 | 解法 |
|---|---|---|
| tensorflow 無 cp314 wheel | Python 3.14 太新 | `uv python pin 3.12` |
| cannot import name 'mjx' | mujoco 4.x 拆出 mjx | 改用鎖定版本 |
| device_put_replicated deprecated | JAX 與 brax 版本不合 | 降版本（見上） |
| TensorBoard No dashboards | 還沒寫出事件檔 | 稍後重新整理 |
| GPU OOM | 顯存不足 | `XLA_PYTHON_CLIENT_MEM_FRACTION=0.7` |
