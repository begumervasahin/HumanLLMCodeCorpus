def process_csv_line(line):
    elements = []
    skip_until = 0
    fields = line.rstrip().split(',')
    i = 0
    while i < len(fields):
        if i <= skip_until:
            i += 1
            continue
        if '"' in fields[i]:
            combined_field = fields[i]
            j = i + 1
            while j < len(fields) and '"' not in fields[j]:
                combined_field += ',' + fields[j]
                j += 1
            combined_field += ',' + fields[j]
            elements.append(combined_field.strip('"'))
            skip_until = j
        else:
            elements.append(fields[i])
        i += 1
    return elements
def find_max_values(file_path):
    max_num_students = 0
    max_stud_staff_ratio = 0.0
    with open(file_path, 'r') as f:
        for line in f:
            csplit = line.rstrip().split(',')
            if csplit[0] == "world_rank":
                continue
            parsed_line = process_csv_line(line)
            try:
                num_students = int(parsed_line[-5])
                student_staff_ratio = float(parsed_line[-4])
                max_num_students = max(max_num_students, num_students)
                max_stud_staff_ratio = max(max_stud_staff_ratio, student_staff_ratio)
            except (ValueError, IndexError):
                continue
    return max_num_students, max_stud_staff_ratio
def write_metadata(max_num_students, max_stud_staff_ratio):
    with open("metadata.txt", 'w') as meta:
        meta.write(f"max_num_students: {max_num_students}\n")
        meta.write(f"max_stud_staff_ratio: {max_stud_staff_ratio:.6f}\n")
def process_universities(file_path, max_num_students, max_stud_staff_ratio):
    with open(file_path, 'r') as f, \
         open("universities.points", 'w') as pts, \
         open("universities.labels", 'w') as lbls:
        for line in f:
            csplit = line.rstrip().split(',')
            if csplit[0] == "world_rank":
                continue
            parsed_line = process_csv_line(line)
            try:
                num_students = float(parsed_line[-5]) / max_num_students
                student_staff_ratio = 1.0 - (float(parsed_line[-4]) / max_stud_staff_ratio)
                university_name = parsed_line[1]
                teaching_score = float(parsed_line[2]) / 100
                total_score = parsed_line[-6]
                lbls.write(university_name + "\n")
                try:
                    total_score = float(total_score) / 100
                except ValueError:
                    total_score = teaching_score
                pts.write(f"{total_score} {num_students} {student_staff_ratio}\n")
            except (ValueError, IndexError):
                continue
def main():
    file_path = "timesData.csv"
    max_num_students, max_stud_staff_ratio = find_max_values(file_path)
    write_metadata(max_num_students, max_stud_staff_ratio)
    process_universities(file_path, max_num_students, max_stud_staff_ratio)
if __name__ == "__main__":
    main()