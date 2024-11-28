from diaries.AbstractDiary import AbstractDiary

class HirotoDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "風邪をひいてしまい、鼻と喉が痛い。"

    def get_author(self):
        return "井上翔人"
