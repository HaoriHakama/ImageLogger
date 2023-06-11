from image_logger.receiver import Receiver
from threading import Thread


class ImageListManeger:
    """
    Image Loggerのバックエンドを統括するクラス

    Attribute
    ---------
    image_list
        画像とテキストのリスト
    receiver: Receiver
        送信されたメッセージを受信するやつ

    """

    def __init__(self) -> None:
        self.image_list: list[dict] = []
        self.receiver = Receiver()
        Thread(target=self._loop, daemon=True).start()

    def _loop(self):
        while True:
            message = self.receiver.msg_q.get()
            if message:
                print(message)
            self.image_list.append(message)

    def get_img(self, index):
        if len(self.image_list) >= index:
            return self.image_list[index]
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
