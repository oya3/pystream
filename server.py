import socket
import argparse
import traceback
import yaml


def main(config):
    server_ip = str(config['ip'])
    server_port = int(config['port'])
    listen_num = 5
    buffer_size = 4096
    # 1.ソケットオブジェクトの作成
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.作成したソケットオブジェクトにIPアドレスとポートを紐づける
    tcp_server.bind((server_ip, server_port))
    # 3.作成したオブジェクトを接続可能状態にする
    tcp_server.listen(listen_num)
    print("server {}:{}".format(server_ip, server_port))
    # 4.ループして接続を待ち続ける
    while True:
        # 5.クライアントと接続する
        client, address = tcp_server.accept()
        print("[*] Connected!! [ Source : {}]".format(address))
        # 6.データを受信する
        data = client.recv(buffer_size)
        print("[*] Received Data : {}".format(data.decode()))
        # 7.クライアントへデータを返す
        message = "ACK!! [{}]".format(data.decode())
        client.send(message.encode())
        # 8.接続を終了させる
        client.close()


def read_config(args):
    config_file = 'server.yaml'
    if args.config:
        config_file = args.config
    with open(config_file, 'r') as yml:
        config = yaml.safe_load(yml)
    return config


if __name__ == '__main__':
    try:
        # 入力引数設定
        parser = argparse.ArgumentParser(description='tcp server')
        parser.add_argument('-c', '--config')  # option: config ファイル指定
        args = parser.parse_args()  # 入力引数取得
        config = read_config(args)
        main(config)
    except Exception:  # # main() で発生する異常はすべてキャッチする
        t = traceback.format_exc()
        print("ERROR: {}".format(t))
