# Changelog

### bug fix 2023.02.19.2330(JST)

いくつかのバグが修正されました

- LOWRAM オプション有効時にエラーになる問題
- Linux でエラーになる問題
- XY plot が正常に終了しない問題
- 未ロードのモデルを設定時にエラーになる問題

### update to version 3 2023.02.17.2020(JST)

- LoRA 関係の機能を追加しました
- Log を保存し、設定を呼び出せるようになりました
- safetensors,fp16 形式での保存に対応しました
- weight のプリセットに対応しました
- XY プロットの予約が可能になりました

### bug fix 2023.02.19.2330(JST)

Several bugs have been fixed

- Error when LOWRAM option is enabled
- Error on Linux
- XY plot did not finish properly
- Error when setting unused models

### update to version 3 2023.02.17.2020(JST)

- Added LoRA related functions
- Logs can now be saved and settings can be recalled.
- Save in safetensors and fp16 format is now supported.
- Weight presets are now supported.
- Reservation of XY plots is now possible.

### bug fix 2023.01.29.0000(JST)

pinpoint blocks が X 方向で使用できない問題を修正しました。
pinpoint blocks 選択時 Triple,Twice を使用できない問題を解決しました
XY plot 使用時に一部軸タイプで MBW を使用できない問題を解決しました
Fixed a problem where pinpoint blocks could not be used in the X axis.
Fixed a problem in which Triple,Twice could not be used when selecting pinpoint blocks.
Problem solved where MBW could not be used with some axis types when using XY plot.

### bug fixed 2023.01.28.0100(JST)

MBW モードで Save current model ボタンが正常に動作しない問題を解決しました
ファイル名が長すぎて保存時にエラーが出る問題を解決しました
Problem solved where the "Save current model" button would not work properly in MBW mode
Problem solved where an error would occur when saving a file with too long a file name

### bug fixed 2023.01.26.2100(JST)

XY plot においてタイプ MBW が使用できない不具合を修正しました
Fixed a bug that type of MBW could work in XY plot

### updated 2023.01.25.0000(JST)

added several features

- added new merge mode "Triple sum","sum Twice"
- added XY plot
- 新しいマージモードを追加しました "Triple sum","sum Twice"
- XY plot 機能を追加しました

### bug fixed 2023.01.20.2350(JST)

png info がうまく保存できない問題を解決しました。
Problem solved where png info could not be saved properly.
