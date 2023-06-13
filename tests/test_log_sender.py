import cv2
import base64
import cv2
import socket
import json


def log_sender(message: dict, port=9010):
    """
    ポート9010番にjson形式でメッセージを送信する
    """

    message["image"] = _cv_to_base64(message["image"])

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", port))

    message_json = json.dumps(message)

    client.send(message_json.encode("utf-8"))

    client.close()


def _cv_to_base64(img):
    _, encoded = cv2.imencode(".jpg", img)
    return base64.b64encode(encoded).decode("ascii")


def main():
    FILE_PATH = ".\sample.png"

    image = cv2.imread(FILE_PATH)
    log_sender({"image": image, "text": "1"})
    image = cv2.imread(FILE_PATH, 0)
    log_sender({"image": image, "text": "1"})


if __name__ == "__main__":
    main()
