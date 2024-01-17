# 前提

- windows10 git-bash 環境でpyenvが動作する環境  
- 詳細は以下を参照すること  
  python で tcp 接続(server/client)でメッセージ送受信する  
  https://blog.oya3.net/posts/2024/01/16/python-stream/

# 実行手順

## exe を利用する場合

### server 起動  

server.yaml は自分の設定に置き換えておく必要がある。localhostのままでもいいがserver,clientは同じ端末で実施する必要がある  
※ server.exeをダブルクリックで起動しても server.exe 直下の server.yaml を読み込んで実行するようになっている  

``` bash
# server.yaml を適宜記載しておくこと
$ cd pystream
$ cd dist
# パターン１：暗黙で同じ階層のserver.yamlを読み込んで起動
$ ./server.exe
# パターン２：-c 省略オプションで指定したserver.yamlを読み込んで起動
$ ./server.exe -c server.yaml
# パターン３：--config オプションで指定したserver.yamlを読み込んで起動
$ ./server.exe --config server.yaml
```

### client 起動  

server.yaml の内容のip,portを指定してメッセージ送信する  

``` bash
$ cd pystream
$ cd dist
$ ./client.exe 127.0.0.1 9901 test
```

## python を利用する場合


### 準備

``` bash
$ cd pystream
# for git-bash
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
```

### server 起動  

``` bash
$ python server.py
$ python server.py -c server.yaml
$ python server.py --config server.yaml
```

### client 起動  

server.yaml の内容のip,portを指定してメッセージ送信する  

``` bash
$ python client.py 127.0.0.1 9901 test
```

# 参考URL

- PythonでTCP通信(サーバ編)
  https://qiita.com/keiusukematsuda/items/aacded313fdb6c08f410
- PythonでTCP通信(クライアント編)
  https://qiita.com/keiusukematsuda/items/362450fda4beca76c030
- ArgumentParserの使い方を簡単にまとめた
  https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0

