from abc import ABC, abstractmethod


class Employee(ABC):
    """
    Lớp trừu tượng đại diện cho nhân viên.
    """

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_info(self):
        print(
            f"Mã NV: {self.employee_id} | "
            f"Họ tên: {self.name} | "
            f"Loại: {self.get_employee_type()}"
        )

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_employee_type(self):
        pass


class FullTimeEmployee(Employee):
    """
    Nhân viên toàn thời gian.
    """

    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

    def get_employee_type(self):
        return "Full-time"


class PartTimeEmployee(Employee):
    """
    Nhân viên bán thời gian.
    """

    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.working_hours * self.hourly_rate

    def get_employee_type(self):
        return "Part-time"


class InternEmployee(Employee):
    """
    Thực tập sinh.
    """

    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)
        self.allowance = allowance

    def calculate_salary(self):
        return self.allowance

    def get_employee_type(self):
        return "Intern"


employees = [
    FullTimeEmployee(
        "E001",
        "Nguyen Van A",
        15000000,
        3000000
    ),
    PartTimeEmployee(
        "E002",
        "Tran Thi B",
        80,
        50000
    ),
    InternEmployee(
        "E003",
        "Le Van C",
        3000000
    )
]


def display_employees(employee_list):
    print("\n--- DANH SÁCH NHÂN VIÊN ---")

    for employee in employee_list:
        employee.display_info()


def display_salaries(employee_list):
    print("\n--- BẢNG LƯƠNG NHÂN VIÊN ---")

    for employee in employee_list:
        salary = employee.calculate_salary()

        print(
            f"{employee.employee_id} | "
            f"{employee.name} | "
            f"Lương: {salary:,.0f} VND"
        )


def main():
    while True:

        print("\n=== EMPLOYEE SALARY MANAGER ===")
        print("1. Xem danh sách nhân viên")
        print("2. Tính lương toàn bộ nhân viên")
        print("3. Thoát chương trình")
        print("================================")

        choice = input(
            "Chọn chức năng (1-3): "
        )

        match choice:
            case "1":
                display_employees(employees)

            case "2":
                display_salaries(employees)

            case "3":
                print(
                    "Cảm ơn bạn đã sử dụng "
                    "Employee Salary Manager!"
                )
                break

            case _:
                print(
                    "Lựa chọn không hợp lệ. "
                    "Vui lòng thử lại."
                )


if __name__ == "__main__":
    main()