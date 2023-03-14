# SuperMerger

- Model merge extention for [AUTOMATIC1111's stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- Merge models can be loaded directly for generation without saving

# Recent Update

すべての更新履歴は[こちら](https://github.com/hako-mikan/sd-webui-supermerger/blob/main/changelog.md)にあります。  
All updates can be found [here](https://github.com/hako-mikan/sd-webui-supermerger/blob/main/changelog.md).

### update 2023.03.03.0145(JST)

- XY プロットに新たな軸「mbw alpha」「mbw beta」「mbw alpha and beta」を追加しました。

### update 2023.03.02.1900(JST)

- Elemental Merge 機能を実装しました。詳細は[こちら](https://github.com/hako-mikan/sd-webui-supermerger/blob/main/elemental_ja.md)

### update 2023.02.20.2000(JST)

"diffusers"をインポートするタイミングを変更しました。このアップデートにより、環境によっては"diffusers"のインストールなしに起動できるようになります。

diffusers のインストールが必要になりました。windows の場合は web-ui のフォルダでコマンドプロンプトから"pip install diffusers"を打つことでインストールできる場合がありますが環境によります。

#

# 概要

この extention ではモデルをマージした際、保存せずに画像生成用のモデルとして読み込むことができます。
これまでマージしたモデルはいったん保存して気に入らなければ削除するということが必要でしたが、この extention を使うことで HDD や SSD の消耗を防ぐことができます。

## 使い方

### マージモード

#### Weight sum

通常のマージです。alpha が使用されます。MBW が有効になっている場合は MBW の base がアルファとして使われます

#### Add difference

差分マージです。MBW が有効になっている場合は MBW の base がアルファとして使われます

#### Triple sum

マージを 3 モデル同時に行います。alpha,beta が使用されます。モデル選択窓が 3 つあったので追加した機能ですが、有効に働かうかはわかりません。MBW でも使えます。それぞれ MBW の alpha,beta を入力してください。

#### sum Twice

Weight sum を 2 回行います。alpha,beta が使用されます。MBW モードでも使えます。それぞれ MBW の alpha,beta を入力してください。

### use MBW

チェックするとブロックごとのマージが有効になります。各ブロックごとの比率は下部のスライダーなどで設定してください。

## 各ボタン

### Merge

マージした後、生成用モデルとして読み込みます。 **左上のモデル情報とは違うモデルがロードされていることに注意してください。** 左上のモデル選択画面でモデルを選択しなおすとリセットされます

### Gen

text2image タブの設定で画像生成を行います

### Merge and Gen

マージしたのち画像を生成します

### Set from ID

マージログから設定を読み込みます。ログはマージが行われるたびに更新され、1 から始まる連番の ID が付与されます。ID を生成される画像や PNG info に記載することも可能で、write merged model ID to から設定してください。-1 で Set をすると最後にマージした設定を読み出します。マージログは extention/sd-webui-supermerger/mergehistory.csv に保存されます。他アプリで開いた状態だと読み取りエラーを起こすので注意してください。History タブで閲覧や検索が可能です。検索は半角スペースで区切ることで and/or 検索が可能です。

### Sequential XY Merge and Generation

連続マージ画像生成を行います。すべてのマージモードで有効です。

#### alpha,beta

アルファ、ベータを変更します。

#### alpha and beta

アルファ、ベータを同時に変更します。アルファ、ベータの間は半角スペースで区切り、各要素はカンマで区切ってください。数字ひとつの場合はアルファベータ共に同じ値が入力されます。  
例: 0,0.5 0.1,0.3 0.4,0.5

#### MBW

階層マージを行います。改行で区切った比率を入力してください。プリセットも使用可能ですが、**改行で区切る**ことに注意をして下さい。Triple,Twice の場合は２行で１セットで入力して下さい。奇数行だとエラーになります。

#### seed

シードを変更します。-1 と入力すると、反対の軸方向には固定された seed になります。

#### model_A,B,C

モデルを変更します。モデル選択窓で選択されたモデルは無視されます。

#### pinpoint blocks

MBW において特定のブロックのみを変化させます。反対の軸は alpha または beta を選んでください。ブロック ID を入力すると、そのブロックのみ alpha(beta)が変わります。他のタイプと同様にカンマで区切ります。スペースまたはハイフンで区切ることで複数のブロックを同時に変化させることもできます。最初に NOT をつけることで変化対象が反転します。NOT IN09-OUT02 とすると、IN09-OUT02 以外が変化します。NOT は最初に入力しないと効果がありません。

##### 入力例

IN01,OUT10 OUT11, OUT03-OUT06,OUT07-OUT11,NOT M00 OUT03-OUT06
この場合

- 1:IN01 のみ変化
- 2:OUT10 および OUT11 が変化
- 3:OUT03 から OUT06 が変化
- 4:OUT07 から OUT11 が変化
- 5:M00 および OUT03 から OUT06 以外が変化

となります。0 の打ち忘れに注意してください。
![xy_grid-0006-2934360860 0](https://user-images.githubusercontent.com/122196982/214343111-e82bb20a-799b-4026-8e3c-dd36e26841e3.jpg)

ブロック ID(大文字のみ有効)
BASE,IN00,IN01,IN02,IN03,IN04,IN05,IN06,IN07,IN08,IN09,IN10,IN11,M00,OUT00,OUT01,OUT02,OUT03,OUT04,OUT05,OUT06,OUT07,OUT08,OUT09,OUT10,OUT11

### XY プロットの予約

Reserve XY plot ボタンはすぐさまプロットを実行せず、ボタンを押したときの設定の XY プロットの実行を予約します。予約した XY プロットは通常の XY プロットが終了した後か、Reservation タブの Start XY plot ボタンを押すと実行が開始されます。予約は XY プロット実行時・未実行時いつでも可能です。予約一覧は自動更新されないのでリロードボタンを使用してください。エラー発生時はそのプロットを破棄して次の予約を実行します。すべての予約が終了するまで画像は表示されませんが、Finished になったものについてはグリッドの生成は終わっているので、Image Browser 等で見ることが可能です。  
「|」を使用することで任意の場所で予約へ移動することも可能です。  
0.1,0.2,0.3,0.4,0.5|0.6,0.7,0.8,0.9,1.0 とすると

0.1,0.2,0.3,0.4,0.5  
0.6,0.7,0.8,0.9,1.0  
というふたつの予約に分割され実行されます。これは要素が多すぎてグリッドが大きくなってしまう場合などに有効でしょう。

### キャッシュについて

モデルをメモリ上に保存することにより連続マージなどを高速化することができます。
キャッシュの設定は web-ui の setting から行ってください。

### unload ボタン

現在ロードされているモデルを消去します。これは kohya-ss の GUI を使用するときなど GPU メモリを開放するときに使用します。消去すると画像の生成はできません。生成する場合にはモデルを選び直して下さい。

## LoRA

LoRA 関連の機能です。基本的には kohya-ss のスクリプトと同じですが、階層マージに対応します。現時点では V2.X 系のマージには対応していません。

### merge to checkpoint

モデルに LoRA をマージします。複数の LoRA を同時にマージできます。  
LoRA 名 1:マージ比率 1:階層,LoRA 名 2:階層,マージ比率 2,LoRA 名 3:マージ比率 3･･･  
と入力します。LoRA 単独でも使用可能です。「:階層」の部分は無くても問題ありません。比率はマイナスを含めどんな値でも入力できます。合計が１にならないといけないという制約もありません(もちろん大きく 1 を越えると破綻します)。

### Make LoRA

ふたつのモデルの差分から LoRA を生成します。
demension を指定すると指定された dimension で作製されます。無指定の場合は 128 で作製します。
alpha と beta によって配合比率を調整することができます。(alpha x Model_A - beta x Model B)　 alpha, beta = 1 が通常の LoRA 作成となります。

### merge LoRAs

ひとつまたは複数の LoRA 同士をマージします。kohya-ss 氏の最新のスクリプトを使用しているので、dimension の異なる LoRA 同氏もマージ可能ですが、dimension の変換の際は LoRA の再計算を行うため、生成される画像が大きく異なる可能性があることに注意してください。

calculate dimention ボタンで各 LoRA の次元を計算して表示・ソート機能が有効化します。計算にはわりと時間がかかって、50 程度の LoRA でも数十秒かかります。新しくマージされた LoRA はリストに表示されないのでリロードボタンを押してください。次元の再計算は追加された LoRA だけを計算します。

### 通常マージと same to Strength の違い

same to Strength オプションを使用しない場合は、kohya-ss 氏の作製したスクリプトのマージと同じ結果になります。この場合、下図のように Web-ui 上で LoRA を適用した場合と異なる結果になります。これは LoRA を U-net に組み込む際の数式が関係しています。kohya-ss 氏のスクリプトでは比率をそのまま掛けていますが、適用時の数式では比率が２乗されてしまうため、比率を 1 以外の数値に設定すると、あるいはマイナスに設定すると Strength（適用時の強度）と異なる結果となります。same to Strength オプションを使用すると、マージ時には比率の平方根を駆けることで、適用時には Strength と比率が同じ意味を持つように計算しています。また、マイナスが効果が出るようにも計算しています。追加学習をしない場合などは same to Strength オプションを使用しても問題ないと思いますが、マージした LoRA に対して追加学習をする場合はだれも使用しない方がいいかもしれません。  
下図は通常適用/same to Strength オプション/通常マージの各場合の生成画像です。figma 化と ukiyoE LoRA のマージを使用しています。通常マージの場合はマイナス方向でも２乗されてプラスになっていることが分かります。
![xyz_grid-0014-1534704891](https://user-images.githubusercontent.com/122196982/218322034-b7171298-5159-4619-be1d-ac684da92ed9.jpg)

階層別マージについては下記を参照してください

https://github.com/bbc-mc/sdweb-merge-block-weighted-gui

このスクリプトでは web-ui、mbw-merge、kohya-ss のスクリプトを一部使用しています
