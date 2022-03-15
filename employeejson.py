class Employee:
    def __init__(self,employee_id,first_name,last_name,position,birth_year,birth_month,birth_day,is_graduated):
        self.employeeid = employee_id
        self.firstname = first_name
        self.lastname = last_name
        self.positioning = position
        self.birthyear = birth_year
        self.birthmonth = birth_month
        self.birthday = birth_day
        self.isgraduate = is_graduated
    def print_data(self):
        print(f"The self.employeeid = {self.employeeid}")
        print(f"The self.firstname = {self.firstname}")
        print(f"The self.lastname = {self.lastname}")
        print(f"The self.positioning = {self.positioning}")
        print(f"The self.birthyear = {self.birthyear}")
        print(f"The self.birthmonth = {self.birthmonth}")
        print(f"The self.birthday = {self.birthday}")
        print(f"The self.isgraduate = {self.isgraduate}")
class EmployeeManager:
    def __init__(self):
        self.employee_dict = {}
    def add_employee(self):
        first_name = self.read_first_name()
        last_name = self.read_last_name()
        position = self.read_position()

        birth_year = self.read_year()
        birth_month = self.read_month()
        birth_day = self.read_day()

        is_graduated = self.read_is_graduated()

        employee_id = self.read_employee_id()

        #self.employee_dict[employee_id] = Employee(employee_id,first_name, last_name, birth_day, birth_month, birth_year, position, is_graduated)
        print("Employee Added!!")
        employee ={"first name": first_name,
                   "last name": last_name,
                   "birth day": birth_day,
                    "birth month": birth_month,
                    "birth year": birth_year,
                    "position": position,
                    "is graduate": is_graduated,
                     "employee id": employee_id }
        return employee





    def remove_employee(self):
        employee_id = self.read_employee_id()
        if employee_id in self.employee_dict:
            del self.employee_dict[employee_id]
            print("Employee Removed!!")
        else:
            print("Employee Id is not valid")

    def update_employee(self):
        employee_id = self.read_employee_id()
        if employee_id in self.employee_dict:
            first_name = self.read_first_name()
            last_name = self.read_last_name()
            birth_year = self.read_year()
            birth_month = self.read_month()
            birth_day = self.read_day()
            position = self.read_position()
            is_graduated = self.read_is_graduated()
            self.employee_dict[employee_id] = Employee(employee_id, first_name, last_name, position,birth_year, birth_month, birth_day,is_graduated)
            print("Employee updated!!")
        else:
            print("Employee Id is not valid")

    def total_employee(self):
        print("Total Employees : " + str(len(self.employee_dict.keys())))

    def print_all(self):
        for i in self.employee_dict:
            print("--> Employee " + str(i) + "=========")
            self.employee_dict[i].print_data()

    def find_employee(self):
        e_id = input(f"Please Enter Employee Id  :")
        if e_id in self.employee_dict:
            self.employee_dict[e_id].print_details()
        else:
            print("Employee Id is not valid")

    def read_first_name(self):
        while True:
            first_name = input("Please Enter The Employee First Name:")
            first_name = first_name.strip()

            if len(first_name) >= 2:
                return first_name
            else:
                print("Error, The Employee First Name should be at least 2 Characters")

    def read_last_name(self):
        while True:
            last_name = input("Please Enter The Employee Last Name:")
            last_name = last_name.strip()

            if len(last_name) >= 2:
                return last_name
            else:
                print("Error, The Employee Last Name should be at least 2 Characters")

    def read_position(self):
        while True:
            position = input("Please Enter The Employee Position:")
            position = position.strip()

            if len(position) >= 1:
                return position
            else:
                print("Error, The Employee Position should be at least 1 Characters")

    def read_year(self):
        while True:
            year_str = input("Please Enter the Employee Birth Year:")
            year_str = year_str.strip()

            if year_str.isdigit():
                year = int(year_str)
                if (year >= 1900) and (year <= 2004):
                    return year
                else:
                    print("Error, The Employee Birth Year should be between 1900 and 2004")
            else:
                print("Error, The Employee Birth Year should be a number")

    def read_month(self):
        while True:
            month_str = input("Please Enter the Employee Birth Month:")
            month_str = month_str.strip()

            if month_str.isdigit():
                month = int(month_str)
                if (month >= 1) and (month <= 12):
                    return month
                else:
                    print("Error, The Employee Birth Month should be between 1 and 12")
            else:
                print("Error, The Employee Birth Month should be a number")

    def read_day(self):
        while True:
            day_str = input("Please Enter the Employee Birth Day:")
            day_str = day_str.strip()

            if day_str.isdigit():
                day = int(day_str)
                if (day >= 1) and (day <= 31):
                    return day
                else:
                    print("Error, The Employee Birth Day should be between 1 and 31")
            else:
                print("Error, The Employee Birth Day should be a number")

    def read_is_graduated(self):
        while True:
            is_graduated_str = input("Have the Employee graduated from the univesity (y/n):")
            is_graduated_str = is_graduated_str.strip()

            if is_graduated_str in ["y", "n"]:
                if is_graduated_str == "y":
                    return True
                else:
                    return False
            else:
                print("Error, Please Enter y or n")

    def read_employee_id(self):
        while True:
            id_str = input("Please Enter the Employee ID:")
            id_str = id_str.strip()

            if id_str.isdigit():
                id = int(id_str)
                if id > 0:
                    return id
                else:
                    print("Error, The Employee ID should be positive number")
            else:
                print("Error, The Employee ID should be a number")


if __name__ == "__main__":
    employee_manager = EmployeeManager()
    all_employees_dict = {}
    while True:
        print("Select from the following option -")
        print("1. Add employee")
        print("2. Remove employee")
        print("3. Update employee")
        print("4. Total employees")
        print("5. Print employees")
        print("6. Find employees")
        print("7.See the logbook")
        print("8.read json file")

        user_choice = int(input("Select 1,2,3,4,5,6,7,8: "))

        if user_choice == 1:
            employee_dict = employee_manager.add_employee()
            employee_id = employee_dict["employee id"]
            #employee_id =self.employee_dict[employee_id]
            all_employees_dict[employee_id] = employee_dict
            print(all_employees_dict)
            from pprint import pprint
            import json
            employee_string = json.dumps(all_employees_dict)
            pprint(employee_string)
            with open("data.json", "w") as jsonfile:
                json.dump(all_employees_dict, jsonfile, indent=4)
            with open("logbook.txt", "at") as file_var:
                file_var.write("User added employee\n")

        elif user_choice == 2:
            employee_manager.remove_employee()
            with open("logbook.txt", "at") as file_var:
                file_var.write("User removed employee\n")
        elif user_choice == 3:
            employee_manager.update_employee()
            with open("logbook.txt", "at") as file_var:
                file_var.write("User updated employee\n")
        elif user_choice == 4:
            employee_manager.total_employee()
            with open("logbook.txt", "at") as file_var:
                file_var.write("User saw the total employee\n")
        elif user_choice == 5:
            employee_manager.print_all()
            with open("logbook.txt", "at") as file_var:
                file_var.write("User printed the total employee\n")
        elif user_choice == 6:
            employee_manager.find_employee()
            with open("logbook.txt", "at") as file_var:
                file_var.write("User found an  employee by employee id\n")
        elif user_choice == 7:
            with open("logbook.txt", "r") as file_var:
                file_lines = file_var.readlines()
                for line in file_lines:
                    print(line.rstrip('\n'))
        elif user_choice == 8:
            import json

            with open("data.json", "r") as my_file:
                employee_dict = json.load(my_file)
                print(employee_dict)


        else:
            print("Invalid choice !!")

