# 08 · Open Duck Mini v2 與 HD-1910 Microduck 復刻：比較

讀取日期 2026-11-19。來源是搜尋摘要與五個社群 repo 的 README／BOM（JoyandAI/OpenMicroDuck、zhuoligetu123/microduck-hd1910m、lumimoon-robotics/microduck-lumi、fanhao375/microduck-replica，另有 harrysungit/microduck-replica 僅讀摘要）。
**這些都是社群專案，描述來自作者自己，我沒有在實機驗證。** Open Duck Mini 的數字來自 docs/01-parts.md（官方 BOM，歐元）。

## 一眼對照
| 項目 | Open Duck Mini v2 | HD-1910 Microduck 復刻 |
|---|---|---|
| 伺服機 | Feetech STS3215 7.4V ×14（官方 BOM 約 €196） | 飛特 HD-1910-C001 ×15；規格 4–8.4 V、堵轉 12 kg·cm；README 標單價 ¥118；你看到的台灣淘寶頁 NT$602.67 |
| 主控 | Raspberry Pi Zero 2 W（供貨不穩、只有 2.4 GHz） | Radxa ZERO 3W（RK3566、2 GB、WiFi，README 標 ¥309）；有預裝系統鏡像（百度網盤） |
| IMU | BNO055（官方 BOM €40，已非新品設計） | LSM6DSV16X，裝在自製 IMU_to_servo 板（¥158），掛在伺服機匯流排上（從機 ID 200） |
| 轉接板 | Waveshare 匯流排轉接板（US$4.99） | Zero Robot HAT（¥228）：**自製板，要在淘寶買** |
| 動作 | 走路為主 | 五個可部署 ONNX：走、站、撿、右踢、前滾翻（觀測 61、動作 14，正規化已烘進模型） |
| 手機控制 | 無（要自己做） | 有 Android APK（zhuoligetu123 repo，內部測試簽名；App 原始碼未公開，只有後端） |
| 模擬訓練 | Open_Duck_Playground（JAX／MJX），官方配方 3 億步 | microduck_rl（mjlab）——就是我們剛跑通的那條流程；HD-1910 BAM 參數放在 microduck_rl 的分支 |
| 伺服機協議 | Feetech STS（Open Duck 軟體已支援） | 飛特 STS/SCS，但 HD-1910 行為接近 HLS 那一行，部分寄存器不支援；官方 Microduck 軟體用 Dynamixel，**協議層要換** |
| 重訓 | 不需要（官方已有訓練好的走路模型） | **換伺服機必須重訓**，不可直接用官方 ONNX；repo 提供已訓練的 HD-1910 ONNX |
| 授權 | 未查 | OpenMicroDuck 同時放了 Apache-2.0 與 CC BY-NC-SA 4.0 兩份授權檔；各自涵蓋什麼**未確認**（NC＝非商業） |

## 已知的坑（HD-1910 版）
- 電池滿電 8.4 V 正好等於 HD-1910 電壓上限，零餘裕。剛充飽別做堵轉測試；裝機前打開過壓保護；堵轉測試電壓建議限制在 5 V 以下。
- 訓練用 BAM 模型沒有硬體 D 增益，真機卻帶 D（出廠 P32／D40），造成顫動；作者把 D 改為 0 且轉矩 1000→850 後，顫動降到約 4–8%。
- 兩份 BAM 參數（飛特官方 vs 陸吾公開）電阻與堵轉力矩估算差很多（2.97 Ω／1.37 N·m 對 4.91 Ω／0.91 N·m），**作者說還沒在真機驗證哪份更準**。
- zhuoligetu123 自己寫：仍有直行偏航、撿東西回穩待完善；起身與翻滾是 App 觸發的模擬驗證，**不能據此宣稱實機驗收**。
- 結構件：HD-1910 舵盤是凸的、XL330 是凹的，同事已改 8 個件重新列印（harrysungit 版）。

## 對我們的意義
**HD-1910 復刻的優點**
1. 現成軟體多：走、站、撿、踢、翻、手機 App、預裝鏡像。
2. 訓練流程就是我們已跑通的 microduck_rl，不必再學 JAX。
3. 伺服機單價低、力矩大；規格書公開（協議、記憶表）。

**HD-1910 復刻的風險**
1. 要買兩塊自製板（HAT ¥228、IMU 板 ¥158），來源是淘寶單一賣家，要確認能否寄台灣、稅額、有無現貨。
2. 協議層與 BAM 參數都是社群摸索，真機驗證少；你會成為除錯者。
3. 可靠度證據是作者自述與模擬影片，不是獨立實測。

**Open Duck Mini 的優點**
1. 零件幾乎都是現成模組，已有你的官方 BOM 與台灣採購表。
2. 我們的 Playground 已能在你的 4090 上訓練（目前 3 億步訓練進行中）。

**Open Duck Mini 的缺點**
1. 動作少（以走路為主），沒有手機 App、撿東西、起身。
2. Pi Zero 2 W 供貨不穩、IMU 已不是新品設計。

## 待決定（未下單前不要鎖死）
- 主線選哪一條，或兩條都做（Open Duck 當學習，HD-1910 當功能版）。
- 淘寶賣家能否出貨台灣，HAT 與 IMU 板是否有現貨。
- HD-1910 版需不需要自己重新辨識 BAM 參數。
