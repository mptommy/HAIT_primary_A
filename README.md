# 自動単語帳作成アプリ
## 概要
- 英語の文章のうちマーカーが引かれている単語を単語帳としてエクセルなどのファイルとして出力する。
## 使用技術
- インスタンスセグメンテーションによって着色部を認識
- OCRによって単語を認識
- EJDict-handを利用して認識した単語の意味を単語帳に保存
