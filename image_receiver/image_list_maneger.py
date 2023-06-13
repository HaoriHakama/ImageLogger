from image_logger.receiver import Receiver
from threading import Thread
from typing import Callable


class ImageListManeger:
    """
    Image Loggerのバックエンドを統括するクラス

    Attribute
    ---------
    image_list
        画像とテキストのリスト
    receiver: Receiver
        送信されたメッセージを受信するやつ
    on_new_img_received: Callable
        表示画像を最新の画像に更新する

    """

    def __init__(self, on_new_img_received: Callable) -> None:
        self.image_list: list[dict] = []
        self.receiver = Receiver()
        self.on_new_img_received = on_new_img_received

        Thread(target=self._loop, daemon=True).start()

    def _loop(self):
        while True:
            message = self.receiver.q.get()
            if message:
                print("receive_message")
                self.image_list.append(message)
                self.on_new_img_received()

                self.receiver.q.task_done()

    def get_img(self, index):
        if len(self.image_list) >= index:
            return self.image_list[index]["image"]
        else:
            try:
                raise IndexError("image_list: index out of range")
            except IndexError as e:
                print(e)

    def del_img(self, index):
        if len(self.image_list) >= index:
            del self.image_list[index]
            return True
        else:
            try:
                raise IndexError("image_list: index out of range")
            except IndexError as e:
                print(e)
                return False

    def del_all_img(self):
        self.image_list = []
        self.index = None

    def save_img(self, index):
        pass
