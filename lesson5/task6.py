sub = {}
with open('task6.txt', 'r', encoding="utf-8") as f:
    for line in f:
        subject, lecture, practice, lab = line.split()
        sub[subject] = int(practice) + int(lecture) + int(lab)
    print(f'Всего проведенных часов по предметам: - \n {sub}')
