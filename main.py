
from diaries.SugamotoDiary import SugamotoDiary
from diaries.K23140Diary import K23140Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  SugamotoDiary(),
  K23140Diary(),] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
