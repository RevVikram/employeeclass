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




    def create_employee_dictionary(self):
        employee_first_name = read_first_name()
        employee_last_name = read_last_name()
        employee_position = read_position()

        employee_birth_year = read_year()
        employee_birth_month = read_month()
        employee_birth_day = read_day()

        employee_is_graduated = read_is_graduated()

        employee_id = read_employee_id()

        employee = {
            "id": employee_id,
            "first_name": employee_first_name,
            "last_name": employee_last_name,
            "position": employee_position,
            "birth_year": employee_birth_year,
            "birth_month": employee_birth_month,
            "birth_day": employee_birth_day,
            "is_graduated": employee_is_graduated
        }
        return employee

    def update_employee_data(self,new_first_name,new_last_name,new_position,new_birth_year,new_birth_month,new_birthday,new_graduation):
        self.new_first_name = new_first_name
        self.new_last_name = new_last_name
        self.new_position = new_position
        self.new_birth_year = new_birth_year
        self.new_birth_month = new_birth_month
        self.new_birth_day = new_birthday
        self.new_graduation = new_graduation
        field_option = read_field_option()
        if field_option == "first_name":
            new_first_name = read_first_name()
            # employee_record = all_employees_dict[employee_id]
            # employee_record['first_name'] = new_first_name
            all_employees_dict[employee_id]['first_name'] = new_first_name
        elif field_option == "last_name":
            new_last_name = read_last_name()
            all_employees_dict[employee_id]['last_name'] = new_last_name
        elif field_option == "position":
            new_position = read_position()
            all_employees_dict[employee_id]['position'] = new_position
        elif field_option == "birth_year":
            new_birth_year = read_year()
            all_employees_dict[employee_id]['birth_year'] = new_birth_year
        elif field_option == "birth_month":
            new_birth_month = read_month()
            all_employees_dict[employee_id]['birth_month'] = new_birth_month
        elif field_option == "birth_day":
            new_birth_day = read_day()
            all_employees_dict[employee_id]['birth_day'] = new_birth_day
        elif field_option == "is graduated":
            new_graduation = read_is_graduated()
            all_employees_dict[employee_id]['is_graduated'] = new_graduation
        else:
            print("enter a valid updation")

def read_option():
    while True:
        user_option = input("This is a list of your options: add: Add an Employee, remove: Remove an Employee, list: List the Employees ,update: Update Employee Data, exit: Exit the app")
        user_option = user_option.strip()

        if user_option in ["add", "remove", "update", "list", "exit"]:
            return user_option
        else:
            print("Error, You should select one of the options in the list")


def read_employee_id():
    while True:
        id_str = input("Please Enter the Employee ID:")
        id_str = id_str.strip()

        if id_str.isdigit():
            id = int(id_str)
            if id > 0 :
                return id
            else:
                print("Error, The Employee ID should be positive number")
        else:
            print("Error, The Employee ID should be a number")


def read_first_name():
    while True:
        first_name = input("Please Enter The Employee First Name:")
        first_name = first_name.strip()

        if len(first_name) >= 2:
            return first_name
        else:
            print("Error, The Employee First Name should be at least 2 Characters")

def read_last_name():
    while True:
        last_name = input("Please Enter The Employee Last Name:")
        last_name = last_name.strip()

        if len(last_name) >= 2:
            return last_name
        else:
            print("Error, The Employee Last Name should be at least 2 Characters")

def read_position():
    while True:
        position = input("Please Enter The Employee Position:")
        position = position.strip()

        if len(position) >= 1:
            return position
        else:
            print("Error, The Employee Position should be at least 1 Characters")

def read_year():
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

def read_month():
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

def read_day():
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

def read_is_graduated():
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
def print_all_employees_data():
    for employee_id_key in all_employees_dict:
        print(f"The data of the employee with Employee_ID = {employee_id_key}")
        print(all_employees_dict[employee_id_key])
def read_field_option():
    while True:
        field_option = input("Please Enter the field you want to update: first_name, last_name, position, birth_year, birth_month, birth_day, is_graduated:")
        field_option = field_option.strip()

        if field_option in ["first_name", "last_name", "position", "birth_year", "birth_month", "birth_day", "is_graduated"]:
            return field_option
        else:
            print("Please enter one of the mentioned fields")

if __name__ == "__main__":
    all_employees_dict = {}
    employee = Employee("employee_id", "first_name", "last_name", "position", "birth_year", "birth_month", "birth_day",
                        "is_graduated")
    while True:
        option = read_option()
        if option == "add":
            print("The user wants to add an Employee")
            employee_dict = employee.create_employee_dictionary()
            employee_id = employee_dict["id"]

            all_employees_dict[employee_id] = employee_dict

            print(all_employees_dict)
        elif option == "remove":
            print("The user wants to remove an Employee")
            employee_id = read_employee_id()
            del all_employees_dict[employee_id]
        elif option == "list":
            print("The user wants a list of the employees")
            print_all_employees_data()
        elif option == "update":
            print("The user wants to update the data of an employee")
            employee_id = read_employee_id()
            employee.update_employee_data("new_first_name","new_last_name","new_position","new_birth_year","new_birth_month","new_birthday","new_graduation")
            print(all_employees_dict)


    #print(employee)
    #employee.print_data()
