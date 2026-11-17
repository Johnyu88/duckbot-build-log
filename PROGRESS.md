# 進度紀錄

狀態：⬜ 未開始　🟨 進行中　✅ 完成

## 里程碑
| 狀態 | 項目 | 備註 |
|---|---|---|
| ✅ | WSL2 訓練環境（JAX CUDA12 + MuJoCo MJX） | 版本已鎖定 |
| ✅ | 首次訓練 + ONNX 匯出 + MuJoCo 模擬預覽 | 1M steps 測試跑約 4 分鐘 |
| ✅ | Fork Open_Duck_Playground 並推送鎖版本 commit | |
| 🟨 | 決定機器人（Open Duck Mini v2 / Microduck 複刻） | 先比 BOM 與 IMU |
| ⬜ | 取得官方 BOM（含數量） | GitHub 需自行下載 |
| ⬜ | 下單零組件 | |
| ⬜ | 3D 列印 | |
| ⬜ | 組裝 | |
| ⬜ | 伺服機 / IMU 測試 | |
| ⬜ | 正式訓練（長時間） | |
| ⬜ | 策略部署到實機 | |
| ⬜ | 與社群共享訓練結果 | |

## 日誌（新的放最上面）

### 2026-11-17
- 訓練環境完成並首次訓練成功（reward 約 14.3 → 24.9）。
- 確認兩隻機器人都有陀螺儀：Open Duck Mini = BNO055；Microduck 官方 = LSM6DSV16X（第三方分析）；複刻版 = BNO080/085/086。
- 建立本專案。
