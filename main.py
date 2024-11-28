from diaries.DiarySample import DiarySample
from diaries.yuyaDiary import yuyaDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), yuyaDiary()] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
