"""全域參數。單位 mm。所有零件只從這裡讀尺寸。"""

# 材料密度 g/cm^3（估重用）
DENSITY = {"PLA": 1.24, "TPU": 1.21}

# 印表機公差檔。
# hole_offset：孔的設計直徑要「加上」多少，印出來才會是名義直徑（孔通常印偏小）。
# outer_offset：外尺寸要加減多少（印出來偏大則填負值）。
# measured=False 表示還沒用公差測試片實測，數值只是暫定。
PRINTERS = {
    "main": {
        "hole_offset": 0.15,
        "outer_offset": 0.0,
        "measured": False,
        "note": "主印表機，暫定值，待實測",
    },
    "old": {
        "hole_offset": 0.30,
        "outer_offset": 0.0,
        "measured": False,
        "note": "不準的那台，先修機構再實測，暫定值",
    },
}

DEFAULT_PRINTER = "main"
