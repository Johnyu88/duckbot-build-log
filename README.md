# 小鴨機器人 Duckbot Build Log

從零開始：買零組件 → 3D 列印 → 組裝 → 測試 → 模擬訓練 → 實機部署，並公開完整過程。

目標機器人（待定，見 [docs/01-parts.md](docs/01-parts.md)）：
- **Open Duck Mini v2**（apirrone，42 cm，Pi Zero 2W + Feetech STS3215 + BNO055 IMU）
- **Microduck**（Pollen Robotics / Hugging Face，25 cm，Dynamixel XL330 + LSM6DSV16X IMU）及其社群複刻版

## 目前進度
見 [PROGRESS.md](PROGRESS.md)。

## 流程文件
| 階段 | 文件 |
|---|---|
| 1. 採購與相容性 | [docs/01-parts.md](docs/01-parts.md) |
| 2. 3D 列印 | [docs/02-printing.md](docs/02-printing.md) |
| 3. 組裝 | [docs/03-assembly.md](docs/03-assembly.md) |
| 4. 測試（伺服機、IMU、通電） | [docs/04-testing.md](docs/04-testing.md) |
| 5. 訓練環境與流程 | [docs/05-training.md](docs/05-training.md) |
| 6. 模型來源與授權 | [hardware/README.md](hardware/README.md) |

## 開發環境
Windows + WSL2 Ubuntu，筆電 RTX 4090 16 GB，uv、JAX CUDA12、MuJoCo MJX。
訓練 fork：<https://github.com/Johnyu88/Open_Duck_Playground>

## 如何參與
開 Issue 回報你的列印/組裝/訓練結果，或發 PR 補充文件。
