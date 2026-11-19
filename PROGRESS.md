# 進度紀錄

狀態：⬜ 未開始　🟨 進行中　✅ 完成

## 里程碑
| 狀態 | 項目 | 備註 |
|---|---|---|
| ✅ | WSL2 訓練環境（JAX CUDA12 + MuJoCo MJX） | 版本已鎖定 |
| ✅ | 首次訓練 + ONNX 匯出 + MuJoCo 模擬預覽 | 1M steps 測試跑約 4 分鐘 |
| ✅ | Fork Open_Duck_Playground 並推送鎖版本 commit | |
| ✅ | 建立 duckbot-build-log 記錄專案 | |
| ✅ | 取得官方 BOM（含數量） | 合計 €387.60，最低估 €321.10，見 docs/01-parts.md |
| ✅ | 取得列印清單與設定 | 36 種零件，見 docs/02-printing.md |
| 🟨 | 決定機器人（Open Duck Mini v2 / Microduck 複刻） | Open Duck Mini 資料最完整，傾向先做它 |
| ✅ | Microduck 模擬訓練與檢視（副線） | 4096 環境訓練、checkpoint 載入、模擬檢視已通；走路行為與 ONNX 待確認 |
| 🟨 | 查台灣來源與價格 | 伺服機已查證，Pi Zero 2 W、BNO055、電芯待逐項查 |
| ⬜ | 補齊 BOM 缺的零件（軸承、喇叭、LED 等） | |
| ⬜ | 下單零組件 | |
| ⬜ | 3D 列印 | |
| ⬜ | 組裝 | |
| ⬜ | 伺服機 / IMU 測試 | |
| ⬜ | 正式訓練（長時間） | |
| ⬜ | 策略部署到實機 | |
| ⬜ | 與社群共享訓練結果 | |

## 日誌（新的放最上面）

### 2026-11-19
- 新增 docs/08：Open Duck Mini 與 HD-1910 Microduck 復刻比較（零件、功能、手機 APK、風險）。HD-1910 版軟體較完整但要買兩塊自製板、真機驗證少；**決定：Open Duck Mini（A，先做）與 HD-1910 Microduck 復刻（B，後做）當作兩台機器人，不是二選一。**Open Duck 3 億步訓練（flat_terrain_backlash）已開跑。
- 割草機：新增 hardware/mower/（規格 v0、系統分解、參考設計對照）。參考資料多為搜尋摘要，尚未驗證；階梯在邊界外；先用手機當大腦加 MCU 當安全層；無人機勘查與車載無人機列為後期階段。
- 新增 docs/07-intent-interface.md：共同意圖介面草案 v0（move/stop/enable/pose/do/health/subscribe 加 goto/dock/lease），尚未實作。
- 新增 docs/06-microduck-runtime-reference.md：讀 Microduck 機上軟體（robotd/btd/mediad/autod/mapd），整理可借用到 Open Duck 與無人車的設計；官方建圖只做二維、ToF 是「手杖」，支持建圖交給無人車的決定。
- Microduck 模擬訓練（4096 環境）跑約 18 小時後手動停止，跌倒率降到 0.21；載入 checkpoint 在模擬檢視器中站穩 2700 步以上沒跌倒。啟用 GPU 繪圖後檢視器從 2 FPS 提升到約 26 FPS。
- ONNX 匯出成功；用最新檢查點（約 46,750 輪）重測：指令 0.2 站著、0.3 約 0.17、0.4 約 0.24 m/s。這與官方 walk「約 0.6 倍指令」的已知特性一致，不需續訓。Microduck 模擬線的目標（跑通訓練→匯出→載入→前進）已達成。細節見 docs/05-training.md。
- 新增 docs/00-vision-roadmap.md：願景、本體加遠端大腦架構、階段路線圖（小鴨為學習平台，巡邏與建圖由無人車承擔）。

### 2026-11-18
- 新增統一 CAD 骨架（hardware/cad，CadQuery）與印表機公差檔；尚未實際執行，公差測試片待印。

### 2026-11-17（下午）
- 整理採購建議表（docs/01-parts.md），部分價格未查證；鋰電池建議在台灣買。

### 2026-11-17（10:20）
- 淘寶找到 STS3215 7.4V 19kg（型號 ST-3215-C001），單價約 NT$462，14 顆約 NT$6,472。
- 確認 Open Duck Mini 與 Microduck 是兩套互不相通的系統（伺服機、電腦、訓練框架都不同），決定先做 Open Duck Mini。
- 讀過 Microduck 訓練環境（mjlab + PyTorch，Python 3.12，需要 CUDA），列為副線，尚未實測。

### 2026-11-17（09:59）
- 讀到官方 BOM：14 顆 STS3215 就佔約 €196，是最大筆開銷；電源是 2 顆 18650 串聯（2S）加 5V 降壓。
- 發現 BOM 沒列出軸承、喇叭、LED、相機、麥克風，要另外補（只想走路的話表情件可後補）。
- 官方列印 15% 填充，MakerWorld 建議 25%，兩者不同，先照官方。
- 確認 IMU：Open Duck Mini = BNO055，BOM 要 €40，官方說有約 1 美元的替代品但沒試過。

### 2026-11-17（上午）
- 訓練環境完成並首次訓練成功（reward 約 14.3 → 24.9）。
- 確認兩隻機器人都有陀螺儀：Open Duck Mini = BNO055；Microduck 官方 = LSM6DSV16X（第三方分析）；複刻版 = BNO080/085/086。
- 建立本專案。
