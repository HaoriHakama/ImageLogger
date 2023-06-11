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
    client.connect(("localhost", port))

    message_json = json.dumps(message)

    client.send(message_json.encode("utf-8"))

    client.close()

def _cv_to_base64(img):
    _, encoded = cv2.imencode(".jpg", img)
    return base64.b64decode(encoded).decode("ascii")