import numpy as np


def process_marks_data(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except IOError:
        print(f"Error: File {file_path} could not be opened.")
        exit()

    # Process the first line to obtain the weighting of the coursework and the number of students.
    first_line = lines[0].split()
    num_students = int(first_line[0])
    coursework_weight = float(first_line[1])
    # Set up the two-dimensional NumPy array for the student information.

    student_records = np.array([[0, 0.0, 0.0, 0.0]] * num_students, dtype=float)
    # Fill in the array with your registration number, exam result, average coursework score, and overall score.

    for i, line in enumerate(lines[1:]):
        parts = line.split()
        reg_num = int(parts[0])
        exam_score = float(parts[1])
        coursework_scores = list(map(float, parts[2:]))
        avg_coursework = np.mean(coursework_scores)
        overall_score = (coursework_weight / 100) * avg_coursework + \
                        ((100 - coursework_weight) / 100) * exam_score

        student_records[i] = [reg_num, exam_score, avg_coursework, overall_score]

    return student_records, coursework_weight


def determine_grade(exam, coursework, overall):
    if exam < 35 or coursework < 35:
        return 'Fail'
    elif overall >= 70:
        return 'First'
    elif 50 <= overall <= 69:
        return 'Second'
    elif 40 <= overall <= 49:
        return 'Third'
    else:
        return 'Fail'


def main():
    file_path = 'ex5data.txt'  # Replace with your actual file path
    student_records, coursework_weight = process_marks_data(file_path)

    # Define the structured array's designated data type.
    student_dtype = np.dtype([('reg_num', 'i4'), ('exam_score', 'i4'),
                              ('coursework_score', 'i4'), ('total_score', 'i4'), ('grade', 'U10')])

    # Set up the structured array that is one dimension.
    structured_data = np.zeros(student_records.shape[0], dtype=student_dtype)

    # Add grades and rounded data to the structured array.
    for i, (reg_num, exam_score, coursework_score, overall_score) in enumerate(student_records):
        grade = determine_grade(exam_score, coursework_score, overall_score)
        structured_data[i] = (reg_num, round(exam_score), round(coursework_score),
                              round(overall_score), grade)

    # Arrange the structured array in decreasing order of overall mark
    sorted_data = np.sort(structured_data, order='total_score')[::-1]

    # Save the array that has been sorted to a file.
    with open('output_file.txt', 'w') as f:
        print(sorted_data, file=f)

    # Compute and produce the statistics for the class.
    first_class = len([s for s in sorted_data if s['grade'] == 'First'])
    second_class = len([s for s in sorted_data if s['grade'] == 'Second'])
    third_class = len([s for s in sorted_data if s['grade'] == 'Third'])
    failed = len([s for s in sorted_data if s['grade'] == 'Fail'])

    print(f"First-class: {first_class}")
    print(f"Second-class: {second_class}")
    print(f"Third-class: {third_class}")
    print(f"Failed: {failed}")

    # Print the students' registration numbers who received first-class grades.
    first_class_regs = [s['reg_num'] for s in sorted_data if s['grade'] == 'First']
    print("Registration numbers of students with first-class marks:")
    print(first_class_regs)


if __name__ == "__main__":
    main()