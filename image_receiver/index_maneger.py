from image_receiver.image_list_maneger import ImageListManeger


class IndexManeger:
    """
    現在表示されている画像のインデックスを管理するクラス

    Attribute
    ---------
    index: int
        現在表示されている画像のインデックス
    list_maneger: ListManeger
        ListManegerのインスタンスオブジェクト
    """

    def __init__(self, list_maneger: ImageListManeger) -> None:
        self._index: int | None = None
        self.list_maneger = list_maneger

    def next_index(self):
        if self._index is not None:
            self.index = min(
                self._index + 1, len(self.list_maneger.image_list) - 1
            )

        return self._index

    def prev_index(self):
        if self._index is not None:
            self._index = max(0, self._index - 1)

        return self._index

    def first_index(self):
        if self._index is not None:
            self._index = 0

        return self.index

    def last_index(self):
        if self.index is not None:
            self._index = len(self.list_maneger.image_list) - 1

        return self._index

    def clear_index(self):
        self._index = None
