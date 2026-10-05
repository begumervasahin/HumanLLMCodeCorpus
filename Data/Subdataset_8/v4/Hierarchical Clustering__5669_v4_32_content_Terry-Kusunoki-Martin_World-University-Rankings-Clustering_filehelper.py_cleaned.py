
with open("timesData.csv", 'r') as f:
    max_num_students = 0
    max_stud_staff_ratio = 0.0
    for line in f:
        columns = line.strip().split(',')
        if columns[0] == "world_rank":
            continue
        new_line = []
        skip_until = 0
        for i in range(len(columns)):
            if i <= skip_until:
                continue
            if '"' in columns[i]:
                new_element = columns[i]
                j = i + 1
                while '"' not in columns[j]:
                    j += 1
                new_element = "".join(columns[i:j + 1]).strip('"')
                new_line.append(new_element)
                skip_until = j
            else:
                new_line.append(columns[i])
        try:
            num_students = int(new_line[-5])
            student_staff_ratio = float(new_line[-4])
            max_num_students = max(max_num_students, num_students)
            max_stud_staff_ratio = max(max_stud_staff_ratio, student_staff_ratio)
        except (ValueError, IndexError):
            continue
with open("metadata.txt", 'w') as meta:
    meta.write("max_num_students: %d\n" % max_num_students)
    meta.write("max_stud_staff_ratio: %f\n" % max_stud_staff_ratio)
with open("timesData.csv", 'r') as f, \
     open("universities.points", 'w') as pts, \
     open("universities.labels", 'w') as lbls:
    for line in f:
        columns = line.strip().split(',')
        if columns[0] == "world_rank":
            continue
        new_line = []
        skip_until = 0
        for i in range(len(columns)):
            if i <= skip_until:
                continue
            if '"' in columns[i]:
                new_element = columns[i]
                j = i + 1
                while '"' not in columns[j]:
                    j += 1
                new_element = "".join(columns[i:j + 1]).strip('"')
                new_line.append(new_element)
                skip_until = j
            else:
                new_line.append(columns[i])
        try:
            num_students = float(new_line[-5]) / max_num_students
            student_staff_ratio = 1.0 - (float(new_line[-4]) / max_stud_staff_ratio)
            name = new_line[0]
            teaching_score = float(new_line[2]) / 100
            tot_score = new_line[-6]
            lbls.write(name + "\n")
            try:
                tot_score = float(tot_score) / 100
            except ValueError:
                tot_score = teaching_score
            pts.write(f"{tot_score} {num_students} {student_staff_ratio}\n")
        except (ValueError, IndexError):
            continue