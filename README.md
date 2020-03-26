# azure-batch-python-sample
Python を使ってのHello World 的な Azure Batch のサンプルです。

Azure Batch では Container を使うツール/Framework として、Batch Shipyardという手法が提供されています。ただし、いきなりそれを使うと、内部の動きが理解しずらい事もありますので、ここではそれも使いません😊

# 解説 Blog

こちらです。
https://qiita.com/dahatake/items/a9eb00b9d38d01d66539

# ファイル

フォルダー構造

```bash
├─ src
|    ├─ app.py                   --- 計算処理
├─ data 
|    └─ src.txt                  --- テスト用ファイル
├─  startupapp
|    ├─ startup.sh               --- 起動スクリプト
|    ├─ fuse_conn_in.cfg         --- 入力フォルダ マウント用の認証情報ファイル
|    └─ fuse_conn_out.cfg        --- 出力フォルダ マウント用の認証情報ファイル
├─  config.py                    --- ジョブ起動時のAzure Servicesへの認証情報
├─  python_quickstart_client.py  --- ジョブ起動
└─  requirements.txt             --- ジョブ起動スクリプト用 Python 関連モジュール
```
