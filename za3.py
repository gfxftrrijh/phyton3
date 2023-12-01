with open('subjects.txt', 'w') as file:
    file.write("informatika: 100(l) 50(pr) 20(lab)\n")
    file.write("fizika: 30(l) 10(lab)\n")
    file.write("fizra: 30(pr)\n")

subject_dict = {}

with open('subjects.txt', 'r') as file:
    for line in file:
        data = line.split(":")
        subject = data[0]
        lessons = [int(i.split('(')[0]) for i in data[1].split() if i.isdigit()]
        total_lessons = sum(lessons)
        subject_dict[subject] = total_lessons

print(subject_dict)