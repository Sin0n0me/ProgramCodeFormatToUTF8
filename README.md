# 使い方(How to use)

1. **check_list.txt**にパス(絶対, 相対パスどちらも対応)を1行毎に区切りに記入します
2. **format_to_utf8.py**を実行します
3. 対象ディレクトリ以下にあるファイルがUTF-8に変更されます
4. UTF-8に変更されたファイルは変更前のファイルがカレントディレクトリ上の**backup**ディレクトリ配下に追加されます

## 注意
仕組みとしてファイルオープン時に文字コードを判定しオープン, その後UTF-8にエンコーディングして保存しているだけなので文字によっては文字化けを起こすことがあります

## 対応拡張子
初期状態での対応拡張子は以下の通りです
* c
* cpp
* h
* hpp
* hlsl
* glsl

### 対応拡張子の追加or削除方法
対応拡張子は`TARGET_FILE_EXTENDS_SAVE_UTF_8`に文字列リストとして入っているので, 変更することで任意の拡張子のみ対応させることもできます

## シグネチャ付き(BOM付き)UTF-8への変更
シグネチャ付き(BOM付き)UTF-8に変更したい場合は`TARGET_FILE_EXTENDS_SAVE_UTF_8_SIG`に追加することで対象拡張子をシグネチャ付き(BOM付き)UTF-8に変更します

## 特定のディレクトリ以下を対象にしたい
`RECURSIVE = False`を`RECURSIVE = True`に変更すると**check_list.txt**で指定したディレクトリ以下を対象とします

## 使用バージョン
Python3.6

## 使用ライブラリ
* os
* glob
* chardet
* shutil

