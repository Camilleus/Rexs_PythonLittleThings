def write_employees_to_file(employee_list, path):
    with open(path, "w") as file:
        for department in employee_list:
            for employee in department:
                file.write(employee + "\n")
    file.close()


employee_list = [['Robert Stivenson,28',
                  'Alex Denver,30'], ['Drake Mikelsson,19']]
write_employees_to_file(employee_list, "employee_data.txt")
