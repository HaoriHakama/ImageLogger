import socket
import json
from queue import Queue
from threading import Thread


class Receiver:

    def __init__(self) -> None:
        self.q = Queue()

    def start_receiver(self):
        Thread(target=self._receive_message, daemon=True).start()

    def _receive_message(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soc.bind(("localhost"), 9008)

        while True:
            data, _ = soc.recvfrom(2048)
            message = data.decode("utf-8")
            message = json.loads(message)
            self.q.put(message)
