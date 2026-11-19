# 統一 CAD：CadQuery（程式碼即設計）

所有我們自己設計的硬體，用 CadQuery 寫成程式，這份資料夾是**唯一來源**。STL／STEP 是產物，不進版本控制。

## 規則（我們的硬體語言）
1. 單位一律 **mm**。
2. 座標：**X 向前、Y 向左、Z 向上**，原點放在零件的主要關節軸心或安裝基準面中心。
3. 所有尺寸只寫在 `params.py`，零件檔只引用參數，不寫死數字。
4. 一個零件一個檔案，放在 `parts/`，檔內提供 `make()` 回傳一個 `cq.Workplane`。
5. 孔徑用 `common.hole_d(名義直徑, 印表機)` 取得，印表機偏差集中在 `params.PRINTERS`。
6. 新零件要在 `build.py` 登記，並寫下**預期外框尺寸**，`build.py` 會自動檢查。
7. 量到的實際公差寫回 `params.PRINTERS`，並在 `hardware/printers/README.md` 記錄日期。

## 使用
```
cd hardware/cad
pip install cadquery
python build.py
```
產物在 `build/`（已被 .gitignore 忽略）。

## 狀態
- ⚠️ 這份程式是在沒有安裝 CadQuery 的環境寫的，**尚未實際執行過**。第一次跑如果報錯，把錯誤貼回來修。
- 第一個零件是公差測試片（`parts/tolerance_coupon.py`），用來量印表機的真實偏差。
- 伺服機座等真實零件，要等量過 STS3215 實物再做，不先猜尺寸。

## SolidWorks 對照
| SolidWorks | CadQuery |
|---|---|
| 草圖 | `Workplane("XY")` 加 `rect`、`circle` |
| 伸長填料 | `extrude()` |
| 伸長切除 | `cutBlind()`、`cutThruAll()`，或建立實體再 `cut()` |
| 孔精靈 | `hole()`、`cboreHole()`、`cskHole()` |
| 圓角、倒角 | `fillet()`、`chamfer()` |
| 陣列 | `pushPoints()`、`rarray()` |
| 配合 | `Assembly().add()` 加 `constrain()` |
| 全域變數 | `params.py` |
