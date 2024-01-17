import socket
import argparse
import traceback


def main(args):
    target_ip = str(args.ip)  # "127.0.0.1"
    target_port = int(args.port)  # 8080
    buffer_size = 4096
    # 1.ソケットオブジェクトの作成
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.サーバに接続
    tcp_client.connect((target_ip, target_port))
    # 3.サーバにデータを送信
    tcp_client.send(str(args.message).encode())
    # 4.サーバからのレスポンスを受信
    response = tcp_client.recv(buffer_size)
    print("[*]Received a response : {}".format(response.decode()))


if __name__ == '__main__':
    try:
        # 入力引数設定
        parser = argparse.ArgumentParser(description='tcp client')
        parser.add_argument('ip', help='ip')
        parser.add_argument('port', help='port')
        parser.add_argument('message', help='message')
        args = parser.parse_args()  # 入力引数取得
        main(args)
    except Exception:  # # main() で発生する異常はすべてキャッチする
        t = traceback.format_exc()
        print("ERROR: {}".format(t))
