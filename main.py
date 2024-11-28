from diaries.DiarySample import DiarySample
from diaries.HirotoDiary import HirotoDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),HirotoDiary() ] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
