from diaries.AbstractDiary import AbstractDiary

class FuruhashiDiary(AbstractDiary):

     def get_date(self):
           return "2024-11-28"
     
     def get_summary(self):
        return "今回のグループワークは睡眠不足だったこともあり、集中力が欠けていた。生活習慣が乱れつつあるため、気をつけたい"
     
     def get_author(self):
        return "古橋暖"