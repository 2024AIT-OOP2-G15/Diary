from diaries.DiarySample import DiarySample
from diaries.FuruhashiDiary import FuruhashiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), 
           FuruhashiDiary(),
           ] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
