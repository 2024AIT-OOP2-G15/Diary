from diaries.AbstractDiary import AbstractDiary

class SugamotoDiary(AbstractDiary):

    def get_date(self):
        return "2024/11/28"

    def get_summary(self):
        return "物理実験が終わりそう。ただ情報システム概論がまだ終わってない。やばい。"

    def get_author(self):
        return "Sugamoto"
