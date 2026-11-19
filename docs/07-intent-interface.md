# 07 · 共同意圖介面（草案 v0）

目的：Open Duck、Microduck 副線、無人車、無人機、潛水艇，都用同一套「意圖」呼叫。
搖桿、手機、桌機 AI、腳本都是客戶端，只送意圖，**不直接碰馬達**。

狀態：草案，尚未實作。命名參考 Microduck 的 `robot.*` API（讀自 `duck-ipc-proto`），
但本表是我們自己的子集與擴充，不保證與官方相容。

## 1. 原則

1. **一個程式獨佔硬體**（本體上的 `robotd` 類程式）。其他人只能送意圖。
2. **安全層在本體**：意圖是否可執行由本體決定；失聯時自己停（deadman）。
3. **所有客戶端同一份契約**：App、搖桿、AI、腳本呼叫完全相同。
4. **訊息格式**：JSON-RPC 2.0，一行一個物件（沿用 Microduck 作法），先走 Unix socket，再包到網路。
5. **串流與控制分開**：影像與高頻狀態走 WebRTC／UDP；設定與低頻指令走藍牙或 TCP。

## 2. 意圖清單（v0）

| 呼叫 | 參數 | 說明 | 適用 |
|---|---|---|---|
| `robot.move` | vx, vy, wz | 速度意圖，單位 m/s、rad/s。持續送；停止送即觸發 deadman | 全部 |
| `robot.stop` | — | 立即零速並站穩／煞車 | 全部 |
| `robot.enable` | on/off | 馬達上電／斷電 | 全部 |
| `robot.relax` | — | 放鬆馬達（**會倒**，不開放給遠端） | 腿式 |
| `robot.head` | pitch, yaw, … | 頭／雲台姿態 | 鴨、無人車雲台 |
| `robot.pose` | 6D 偏移 | 身體姿態指令（x,y,z,roll,pitch,yaw） | 腿式 |
| `robot.do` | skill 名稱 | 預錄動作：站、坐、撿、起身 | 腿式 |
| `robot.skills` | — | 列出可用動作 | 全部 |
| `robot.loadPolicy` | 名稱 | 切換策略（走路、跑步…） | 腿式 |
| `robot.mode` / `robot.setMode` | mode | 例如 walk、roller、autonomous | 全部 |
| `robot.health` | — | 健康：馬達溫度、電壓、錯誤、IMU | 全部 |
| `robot.state` | — | 目前狀態快照 | 全部 |
| `robot.subscribe` | 欄位, 頻率 | 狀態串流（走高頻通道） | 全部 |
| `robot.shutdown` | — | 關機 | 全部 |
| `system.info` | — | 名稱、版本、硬體 | 全部 |
| `net.status/scan/connect` | … | wifi 設定（走藍牙） | 全部 |

我們額外要加的（Microduck 沒有或不同）：

| 呼叫 | 說明 |
|---|---|
| `robot.goto` | 目標點意圖（交給本體或大腦做路徑），無人車用 |
| `robot.dock` | 回充意圖 |
| `sensor.subscribe` | 光達、深度、相機的串流入口 |
| `brain.lease` | 遠端大腦申請控制權，帶逾時，到期自動交還（見下） |

## 3. 遠端大腦的控制權（lease）

桌機 AI 要開車，不應永久佔著。設計：

- 大腦先 `brain.lease(ttl_ms)` 取得控制權，之後每次 `robot.move` 都會續約。
- 超過 `ttl_ms` 沒收到：本體收回，執行 `robot.stop`。
- 搖桿或本機急停**永遠優先**於 lease。
- Microduck 的 `autod` 也是同樣精神：一般客戶端、隨時可殺，deadman 讓機器人自己停。（`[safety] deadman_ms` 預設 500。）

## 4. 還沒決定的事

- 傳輸：直接用 Microduck 同樣的 Unix socket 加 WebRTC，還是我們自己的 TCP／UDP。
- 驗證：區網內是否要 PIN 或簽章（Microduck 的區網 UDP 搖桿是無驗證，文件明說只限信任網路）。
- 不同機型（腿、輪、飛、潛）的單位與限幅，如何在 `system.info` 宣告。
- `robot.relax` 之類危險呼叫是否只允許本機。
