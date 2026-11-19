# 割草機 · 參考設計對照 v0

讀取日期 2026-11-19。**全部來自搜尋結果摘要，尚未打開各專案的 repo／規格書驗證。**
空白格 = 搜尋沒有找到，不要當成 0 或不存在。

## 商用小型機（尺寸量級參考）
| 機型 | 尺寸 mm | 驅動 | 輪徑 | 電池 | 其他 | 來源 |
|---|---|---|---|---|---|---|
| Segway Navimow i 系列 | 545×385×285；603×468×274（不同型號） | 多為後輪驅動 | | | 防護 IP66，噪音 54–58 dB | navimow.segway.com / ca.navimow.com |
| RURIS Sentinel 1500 | | 4WD | 前 200／後 150 mm | 20 V 6 Ah | 衛星導航 | ruris.ro |
| FJD RM21（大型，非我們量級） | 1330×853×980 | | | 4 kWh | 重 170 kg，最大爬坡 ≤ 20° | fjdynamics.com |

## 自製／改裝參考
| 專案 | 取用什麼 | 備註 |
|---|---|---|
| Ardumower／Sunray | 底盤與 CAD、PCB、RTK 韌體 | 需 Ardumower 底盤與馬達、Arduino Due 或 Grand Central M4、ZED-F9P。尺寸本次**未取得** |
| OpenMower | 軟體、RTK、狀態機；改裝現成割草機 | 硬體清單約 €700（不含割草機與 RTK 基準站）；授權 CC BY-NC-SA 4.0（非商業） |
| SimpleMower | 單檔 Python 控制迴圈範例 | BeagleBone Blue 加 SparkFun RTK |
| Super Droid 割草機底盤套件（大型） | 後輪驅動加前萬向輪的布局 | 13" 驅動輪、6" 萬向輪、24 V 輪椅馬達、2×12 V 35 Ah，約 180 lb；比我們大一個量級 |
| Chalmers 碩士論文 | 可調高度輪組、ESP32 加 BLDC 驅動 | 概念驗證 |
| Project Robokut（RobotShop） | 輪徑與割草高度的關係 | 見下 |

## 可用於 CAD 的推論（待驗證）
- 商用小型機約 55–60 × 40–47 × 27–29 cm，與我們預設的 50×40×25 cm 同量級。
- 輪徑：Robokut 提到割草高度 1.5–3.75 吋，需要 7–8 吋輪才有足夠離地間隙。Sentinel 1500 的輪徑則是 150–200 mm。
- 佈局：後輪驅動加前萬向輪最常見；4WD 在商用機也有。我們 12° 坡是否需要 4WD，要實測。
- 防水：商用機有做到 IP66，我們至少要規劃 IPX4 以上的外殼與接頭（待定）。

## 下一步（未做）
1. 打開 Ardumower 的 CAD／BOM，取得實際底盤尺寸、輪徑、馬達規格與重量。
2. 打開 OpenMower 文件的硬體清單與安全設計。
3. 把以上填入 `hardware/mower/params.py` 起草。
