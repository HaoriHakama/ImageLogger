import flet as ft
from typing import Callable

from image_logger.image_list_maneger import ImageListManeger
from image_logger.index_maneger import IndexManeger


class ControlBar(ft.UserControl):
    """ """

    def __init__(
        self,
        image_list_maneger: ImageListManeger,
        index_maneger: IndexManeger,
        update_image: Callable,
    ):
        super().__init__()
        self.image_list_maneger = image_list_maneger
        self.index_maneger = index_maneger
        self.update_image = update_image

    def build(self):
        skip_buttons = ft.Container(
            ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.SKIP_PREVIOUS_OUTLINED,
                    ),
                    ft.IconButton(
                        icon=ft.icons.SKIP_PREVIOUS,
                    ),
                    ft.IconButton(icon=ft.icons.SKIP_NEXT),
                    ft.IconButton(icon=ft.icons.SKIP_NEXT_OUTLINED),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=ft.colors.BLUE_100,
            border_radius=ft.border_radius.all(10),
            width=300,
        )

        ctrl_buttons = ft.Container(
            ft.Row(
                [
                    ft.IconButton(icon=ft.icons.DELETE),
                    ft.IconButton(icon=ft.icons.DELETE_OUTLINED),
                    ft.IconButton(icon=ft.icons.SAVE_ALT),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=ft.colors.BLUE_100,
            border_radius=ft.border_radius.all(10),
            width=225,
        )

        return ft.Container(
            content=ft.Row(
                [skip_buttons, ctrl_buttons],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    def on_skip_first_clicked(self, e):
        # Indexを最初に戻す
        index = self.index_maneger.first_index()
        if index is None:
            return
        # Indexに該当する画像を取得
        image = self.image_list_maneger.get_img(index)
        # 表示画像を更新
        self.update_image(image)
        e.page.update()

    def on_skip_prev_clicked(self, e):
        pass

    def on_skip_next_clicked(self, e):
        pass

    def on_skip_latest_clicked(self, e):
        pass

    def on_clear_clicked(self, e):
        pass

    def on_clear_all_clicked(self, e):
        pass

    def on_save_clicked(self, e):
        pass
