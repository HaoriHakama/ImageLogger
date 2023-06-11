import socket
import json
from queue import Queue
from threading import Thread


class Receiver:
    def __init__(self) -> None:
        self.msg_q = Queue()
        self.start_server_thread()

    def start_server_thread(self):
        _ = Thread(target=self._start_server, daemon=True).start()

    def _handle_client(self, client_socket: socket):
        while True:
            message_json = client_socket.recv(1024).decode("utf-8")

            if message_json:
                message = json.loads(message_json)
                self.msg_q.put(message)
            else:
                break

        client_socket.close()

    def _start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("127.0.0.1", 9008))
        server.listen(5)

        client_socket, _ = server.accept()

        client_handler = Thread(
            target=self._handle_client, args=(client_socket,), daemon=True
        )
        client_handler.start()
