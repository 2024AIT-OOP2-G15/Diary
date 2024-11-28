from diaries.k23064Diary import k23064Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [k23064Diary(),] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
