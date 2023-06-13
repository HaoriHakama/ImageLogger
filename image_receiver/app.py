import flet as ft
from pathlib import Path

from image_receiver.image_list_maneger import ImageListManeger
from image_receiver.index_maneger import IndexManeger
from image_receiver.control_bar import ControlBar


APP_TITLE = "Image Logger"


class App:
    def main(self, page: ft.Page):
        def on_new_img_received():
            """
            画像が更新された時に最新の画像を表示する
            """
            index = self.index_maneger.last_index()
            image = self.image_list_maneger.get_img(index)
            self.update_img_src(image)
            page.update()

        page.title = APP_TITLE
        page.window_width, page.window_height = 960, 540

        self.image_list_maneger = ImageListManeger(on_new_img_received)
        self.index_maneger = IndexManeger(self.image_list_maneger)

        self.image = ft.Image(
            src_base64=self._load_noimage(),
            width=720,
            fit=ft.ImageFit.FIT_WIDTH,
        )

        self.image_container = ft.Container(
            content=self.image,
            alignment=ft.alignment.center,
            width=720,
            height=405,
        )

        self.text_container = ft.Container(
            content=ft.ListView(expand=True, spacing=10),
            bgcolor=ft.colors.WHITE,
            width=200,
            height=480,
            border=ft.border.all(2, ft.colors.BLUE_200),
        )

        self.container = ft.Container(
            content=ft.Row(
                [
                    ft.Column(
                        controls=[
                            self.image_container,
                            ControlBar(
                                self.image_list_maneger,
                                self.index_maneger,
                                self.update_img_src,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    self.text_container,
                ],
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        )

        page.add(self.container)

    def update_img_src(self, image: str):
        """
        表示する画像のソースを変更する
        """
        self.image.src_base64 = image

    def _load_noimage(self) -> str:
        img_path = Path(r".\src_img\no_image_irasutoya.txt")

        with img_path.open(mode="r", encoding="UTF-8") as f:
            img_base64 = f.read()
        return img_base64

def start():
    ft.app(target=App().main)
