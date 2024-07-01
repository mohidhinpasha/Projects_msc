def display_filtered_employees(employee_data, salary_min, salary_max):
    """
   Employee names and titles are displayed along with a pay range filter.

     Returns:
        None
    """

    # Verify that salary_min and salary_max are equal or less.
    if salary_min > salary_max:
        salary_min, salary_max = salary_max, salary_min

    # Select workers who make the range of salaries
    filtered_employees = [
        (name, title) for name, title, salary in employee_data
        if salary_min <= salary <= salary_max
    ]

    # Arrange workers according to pay (descending order)
    sorted_employees = sorted(filtered_employees, key=lambda x: x[1], reverse=True)

    # Verify if any workers are present.
    if not sorted_employees:
        print("No employees found within the salary range.")
    else:
        # Print the formatted table's heading.
        print(f"{'Name':<20} {'Job Title':<30}")

        # Show employee information, including title and name
        for name, title in sorted_employees:
            print(f"{name:<20} {title:<30}")


def read_employee_data_from_file():
    """
   a collection of tuples is returned after reading employee data from a file.

    Returns:
        list: A collection of tuples with the name, title, and pay of each employee.
    """

    while True:
        try:
            filename = input("Please enter the file name: ")
            with open(filename, 'r') as file:
                employee_data = [
                    (line.strip().split(',')) for line in file
                ]
            # Create tuples (name, title, and salary) from the data.
            employee_data = [(name, title, int(salary))
                              for name, title, salary in employee_data]
            return employee_data
        except FileNotFoundError:
            print("File not found. Please try again.")


def main():
    """
    Loop in the main program to read data, filter workers, and show outcomes.
    """

    #Access employee information from the file.
    employee_data = read_employee_data_from_file()

    # Loop to obtain the wage range and to select the workforce
    while True:
        try:
            salary_start = input("Enter the start of the salary range: ")
            salary_end = input("Enter the end of the salary range: ")

            # Convert inputs for salaries to integers
            salary_start = int(salary_start)
            salary_end = int(salary_end)

            # Verify the salary entry (positive only).
            if salary_start < 0 or salary_end < 0:
                raise ValueError("Salaries must be non-negative.")

            # Use the employee filtering and displaying mechanism.
            display_filtered_employees(employee_data, salary_start, salary_end)

            # Request the user's exit or continue
            if input("Do you wish to quit? (yes/no): ").lower() == 'yes':
                break
        except ValueError as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()