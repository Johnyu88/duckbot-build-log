"""割草機 CAD 參數（單一來源）v0。

所有數值都是**估計起點**，尚未驗證，單位 mm、kg。
來源與依據見 reference-designs.md。要加工前再凍結。
"""

# --- 車體（商用小型機量級 545x385x285 ~ 603x468x274）---
BODY_L = 550.0
BODY_W = 400.0
BODY_H = 270.0

# --- 輪子（Robokut：割草高度 1.5-3.75 吋需 7-8 吋輪；商用機 150-200 mm）---
DRIVE_WHEEL_D = 200.0      # 後驅動輪，待依坡度與離地間隙定案
CASTER_WHEEL_D = 150.0     # 前萬向輪
TRACK_WIDTH = 330.0        # 左右輪中心距（待定）
WHEELBASE = 330.0          # 前後輪軸距（待定）
GROUND_CLEARANCE = 60.0    # 車底離地（待定）

# --- 刀盤（規格 v0：割幅 20-25 cm）---
CUT_WIDTH = 220.0
CUT_HEIGHT_MIN = 25.0
CUT_HEIGHT_MAX = 70.0

# --- 電源（規格 v0：24 V 鋰電＋BMS）---
BATTERY_V = 24.0
BATTERY_BAY = (200.0, 120.0, 90.0)   # 長寬高，待選定電池後再改

# --- 安全 ---
TILT_LIMIT_DEG = 12.0       # 運轉限制；設計能力 >= 15 度
CLIFF_SENSOR_FORWARD = 20.0 # 向下 ToF 離車頭距離，視野不可被外殼擋住（待定）
GEOFENCE_STAIR_MARGIN = 500.0  # 階梯邊緣外退距離

# --- 預留 ---
LANDING_PAD = None          # 階段 3 才定，先預留頂板座位置
TOTAL_MASS_KG = None        # 待 BOM 完成後估算

# 尚未決定：二驅或四驅；輪胎花紋；外殼防護等級（至少 IPX4，商用機達 IP66）
