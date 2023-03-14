# Elemental Merge

- 階層マージを越えた階層マージです

階層マージでは 25 の階層ごとにマージ比率を変えることができますが、階層もまた複数の要素で構成されており、要素ごとに比率を変えることも原理的には可能です。可能ですが、要素の数は 600 以上にもなり人の手で扱えるのかは疑問でしたが実装してみました。いきなり要素ごとのマージは推奨されません。階層マージにおいて解決不可能な問題が生じたときに最終調節手段として使うことをおすすめします。  
次の画像は OUT05 層の要素を変えた結果です。左端はマージ無し。2 番目は OUT05 層すべて(つまりは普通の階層マージ),以降が要素マージです。下表のとおり、attn2 などの中にはさらに複数の要素が含まれます。
![](https://raw.githubusercontent.com/hako-mikan/sd-webui-supermerger/images/sample1.jpg)

## 使い方

要素マージは通常マージ、階層マージ時どちらの場合でも有効で、最後に計算されるために、階層マージで指定した値は上書きされることに注意してください。

Elemental Merge で設定します。ここにテキストが設定されていると自動的に適応されるので注意して下さい。各要素は下表のとおりですが、各要素のフルネームを入力する必要はありません。  
ちゃんと効果が現れるかどうかは print change チェックを有効にすることで確認できます。このチェックを有効にするとマージ時にコマンドプロンプト画面に適用された要素が表示されます。  
部分一致で指定が可能です。

### 書式

階層:要素:比率,階層:要素:比率,...  
または  
階層:要素:比率  
階層:要素:比率  
階層:要素:比率

カンマまたは改行で区切ることで複数の指定が可能です。カンマと改行は混在しても問題ありません。
階層は大文字で BASE,IN00-M00-OUT11 まで指定でます。空欄にするとすべての階層に適用されます。スペースで区切ることで複数の階層を指定できます。
要素も同様でスペースで区切ることで複数の要素を指定できます。  
部分一致で判断するので、例えば「attn」と入力すると attn1,attn2 両方が変化します。「attn2」の場合は attn2 のみ。さらに細かく指定したい場合は「attn2.to_out」などと入力します。

OUT03 OUT04 OUT05:attn2 attn1.to_out:0.5

と入力すると、OUT03,OUT04,OUT05 層の attn2 が含まれる要素及び attn1.to_out の比率が 0.5 になります。
要素の欄を空欄にすると指定階層のすべての要素が変わり、階層マージと同じ効果になります。
指定が重複する場合、後に入力された方が優先されます。

OUT06:attn:0.5,OUT06:attn2.to_k:0.2

と入力した場合、OUT06 層の attn2.to_k 以外の attn は 0.5,attn2.to_k のみ 0.2 となります。

最初に NOT と入力することで効果範囲を反転させることができます。
これは階層・要素別に設定できます。

NOT OUT04:attn:1

と入力すると OUT04 層以外の層の attn に比率 1 が設定されます。

OUT05:NOT attn proj:0.2

とすると、OUT05 層の attn と proj 以外の層が 0.2 になります。

## XY plot

elemental 用の XY plot を複数用意しています。入力例は sample.txt にあります。

#### elemental

複数の要素マージについて XY plot を作成します。要素同士は空行で区切ってください。
トップ画像は sample.txt の sample1 を実行した結果です。

#### pinpoint element

特定の要素について値を変えて XY plot を作成します。pinpoint Blocks と同じことを要素で行います。反対の軸には alpha を指定してください。要素同士は改行またはカンマで区切ります。  
以下の画像は sample.txt の sample3 を実行した結果です。
![](https://raw.githubusercontent.com/hako-mikan/sd-webui-supermerger/images/sample3.jpg)

#### effective elenemtal checker

各要素の影響度を差分として出力します。オプションで anime gif、csv ファイルを出力できます。gif.csv ファイルは output フォルダに ModelA と ModelB から作られるフォルダ下に作成される diff フォルダに作成されます。ファイル名が重複する場合名前を変えて保存しますが、増えてくるとややこしいので diff フォルダを適当な名前に変えることをおすすめします。  
改行またはカンマで区切ります。反対の軸は alpha を使用し、単一の値を入力してください。これは要素の効果を見るのにも有効ですが、要素を指定しないことで階層の効果を見ることも可能なので、そちらの使い方をする場合が多いかもしれません。  
以下の画像は sample.txt の sample5 を実行した結果です。
![](https://raw.githubusercontent.com/hako-mikan/sd-webui-supermerger/images/sample5-1.jpg)
![](https://raw.githubusercontent.com/hako-mikan/sd-webui-supermerger/images/sample5-2.jpg)

### 要素一覧

基本的には attn が顔や服装の情報を担っているようです。特に IN07,OUT03,OUT04,OUT05 層の影響度が強いようです。階層によって影響度が異なることが多いので複数の層の同じ要素を同時に変化させることは意味が無いように思えます。
null と書かれた場所には要素が存在しません。
||IN00|IN01|IN02|IN03|IN04|IN05|IN06|IN07|IN08|IN09|IN10|IN11|M00|M00|OUT00|OUT01|OUT02|OUT03|OUT04|OUT05|OUT06|OUT07|OUT08|OUT09|OUT10|OUT11
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
op.bias|null|null|null||null|null||null|null||null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null
op.weight|null|null|null||null|null||null|null||null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null
emb_layers.1.bias|null|||null|||null|||null|null|||||||||||||||
emb_layers.1.weight|null|||null|||null|||null|null|||||||||||||||
in_layers.0.bias|null|||null|||null|||null|null|||||||||||||||
in_layers.0.weight|null|||null|||null|||null|null|||||||||||||||
in_layers.2.bias|null|||null|||null|||null|null|||||||||||||||
in_layers.2.weight|null|||null|||null|||null|null|||||||||||||||
out_layers.0.bias|null|||null|||null|||null|null|||||||||||||||
out_layers.0.weight|null|||null|||null|||null|null|||||||||||||||
out_layers.3.bias|null|||null|||null|||null|null|||||||||||||||
out_layers.3.weight|null|||null|||null|||null|null|||||||||||||||
skip_connection.bias|null|||null||null|null|||null|null|null|null|null||||||||||||
skip_connection.weight|null|||null||null|null|||null|null|null|null|null||||||||||||
norm.bias|null|||null|||null|||null|null|null||null|null|null|null|||||||||
norm.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
proj_in.bias|null|||null|||null|||null|null|null||null|null|null|null|||||||||
proj_in.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
proj_out.bias|null|||null|||null|||null|null|null||null|null|null|null|||||||||
proj_out.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.attn1.to_k.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.attn1.to_out.0.bias|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.attn1.to_out.0.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.attn1.to_q.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.attn1.to_v.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.attn2.to_k.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.attn2.to_out.0.bias|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.attn2.to_out.0.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.attn2.to_q.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.attn2.to_v.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.ff.net.0.proj.bias|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.ff.net.0.proj.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.ff.net.2.bias|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.ff.net.2.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.norm1.bias|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.norm1.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.norm2.bias|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.norm2.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.norm3.bias|null|||null|||null|||null|null|null||null|null|null|null|||||||||
transformer_blocks.0.norm3.weight|null|||null|||null|||null|null|null||null|null|null|null|||||||||
conv.bias|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null||null|null||null|null||null|null|null
conv.weight|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null||null|null||null|null||null|null|null
0.bias||null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|
0.weight||null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|
2.bias|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|
2.weight|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|
time_embed.0.weight||null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|
time_embed.0.bias||null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|
time_embed.2.weight||null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|
time_embed.2.bias||null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|null|
