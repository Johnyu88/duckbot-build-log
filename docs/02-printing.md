# 02 3D 列印

## 檔案來源
官方 STL 在 `apirrone/Open_Duck_Mini`（`v2` 分支）的 `print/` 資料夾，共 36 個檔案，約 132 MB。本倉庫不收錄 STL，請自行下載（見 [hardware/README.md](../hardware/README.md)）。

## 官方設定（print_guide.md）
- 材料：標準 PLA，填充 **15%**
- 例外：`foot_bottom_tpu.stl` 用 **TPU，填充 40%**

> 注意：MakerWorld 頁面的建議是 0.2 mm 層高、2 層外牆、**25% 填充**，共 6 個盤、約 52.8 小時。兩者的填充率不同，先照官方 GitHub 的 15% 即可，需要更強再提高。

## 要印的零件與數量（共 36 種）
| 部位 | 零件 | 數量 |
|---|---|---|
| 腳 | foot_top | 2 |
| | foot_side | 2 |
| | foot_bottom_pla | 2 |
| | foot_bottom_tpu（TPU） | 2 |
| 腿 | knee_to_ankle_left_sheet | 4 |
| | knee_to_ankle_right_sheet | 4 |
| | leg_spacer | 4 |
| | left_roll_to_pitch | 1 |
| | right_roll_to_pitch | 1 |
| | roll_motor_bottom | 2 |
| | roll_motor_top | 2 |
| 軀幹 | trunk_bottom | 1 |
| | trunk_top | 1 |
| 脖子與頭 | neck_left_sheet | 1 |
| | neck_right_sheet | 1 |
| | head_pitch_to_yaw | 1 |
| | head_yaw_to_roll | 1 |
| | head_roll_mount | 1 |
| | head | 1 |
| | head_bot_sheet | 1 |
| | left_antenna_holder | 1 |
| | right_antenna_holder | 1 |
| | left_cache | 1 |
| | right_cache | 1 |
| 身體 | body_front | 1 |
| | body_middle_bottom | 1 |
| | body_middle_top | 1 |
| | body_back | 1 |
| | battery_pack_lid | 1 |
| 表情（可後補） | bulb | 1 |
| | flash_light_module | 1 |
| | flash_reflector_interface | 1 |
| | left_eye | 1 |
| | right_eye | 1 |
| | speaker_interface | 1 |
| | speaker_stand | 1 |

`print/mods/` 裡有社群改版（Justins_Park_Head_Mod、v2_Jaimes_Mods），原版跑通前先不用。

## 建議印的順序
1. 先印 **腳**（foot_*，含 TPU）和 **一條腿**，用來確認公差與螺帽嵌入
2. 再印軀幹、身體
3. 最後印頭、脖子和表情件（不影響走路）

## 紀錄表
| 零件 / 盤 | 材料 | 時間 | 結果 | 照片 | 備註 |
|---|---|---|---|---|---|
| | | | | | |

## 心得
（列印失敗、公差調整、支撐設定等）
