def process_times_data():
    with open("timesData.csv", 'r') as input_file, \
         open("universities.points", 'w') as points_file, \
         open("universities.labels", 'w') as labels_file, \
         open("metadata.txt", 'w') as metadata_file:
        max_num_students = 0
        max_stud_staff_ratio = 0.0
        for line in input_file:
            columns = line.strip().split(',')
            if columns[0] == "world_rank":
                continue
            processed_columns = []
            skip_until = 0
            for i, column in enumerate(columns[skip_until:], skip_until):
                if '"' in column:
                    new_element = column
                    j = i + 1
                    while '"' not in columns[j]:
                        j += 1
                    new_element = "".join(columns[i:j + 1]).strip('"')
                    processed_columns.append(new_element)
                    skip_until = j
                else:
                    processed_columns.append(column)
            try:
                num_students = int(processed_columns[-5])
                student_staff_ratio = float(processed_columns[-4])
                max_num_students = max(max_num_students, num_students)
                max_stud_staff_ratio = max(max_stud_staff_ratio, student_staff_ratio)
            except ValueError:
                continue
        metadata_file.write("max_num_students: %d\n" % max_num_students)
        metadata_file.write("max_stud_staff_ratio: %f\n" % max_stud_staff_ratio)
        input_file.seek(0)
        for line in input_file:
            columns = line.strip().split(',')
            if columns[0] == "world_rank":
                continue
            processed_columns = []
            skip_until = 0
            for i, column in enumerate(columns[skip_until:], skip_until):
                if '"' in column:
                    new_element = column
                    j = i + 1
                    while '"' not in columns[j]:
                        j += 1
                    new_element = "".join(columns[i:j + 1]).strip('"')
                    processed_columns.append(new_element)
                    skip_until = j
                else:
                    processed_columns.append(column)
            try:
                num_students = float(processed_columns[-5]) / max_num_students
                student_staff_ratio = 1.0 - (float(processed_columns[-4]) / max_stud_staff_ratio)
                name = processed_columns[0]
                teaching_score = float(processed_columns[2]) / 100
                total_score = processed_columns[-6]
                labels_file.write(name + "\n")
                try:
                    total_score = float(total_score) / 100
                except ValueError:
                    total_score = teaching_score
                points_file.write(f"{total_score} {num_students} {student_staff_ratio}\n")
            except ValueError:
                continue
if __name__ == "__main__":
    process_times_data()