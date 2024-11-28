from diaries.DiarySample import DiarySample
from diaries.DiaryRyoei import DiaryRyoei

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           DiaryRyoei(),
           ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
