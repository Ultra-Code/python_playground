from typing import TypedDict


class Employee(TypedDict):
    id: int
    name: str
    department: str


EmployeeList = list[Employee]

# Input data: List of dictionaries
employee_list: EmployeeList = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Management"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"},
]


# Function to be passed to the map() function. Do not change this.
def mod(employee: Employee) -> str:
    return employee["name"] + "_" + employee["department"]


def to_mod_list(employees: EmployeeList) -> list[str]:
    return [mod(employee) for employee in employees]


def generate_usernames(userlist: list[str]) -> list[str]:
    return [user.replace(" ", "_") for user in userlist]


def map_id_to_initial(employees: EmployeeList) -> dict[str, int]:
    return {employee["name"][0]: employee["id"] for employee in employees}


def main() -> None:
    mod_emp_list = to_mod_list(employee_list)
    print("Modified employee list: " + str(mod_emp_list) + "\n")

    print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

    print(f"Initials and ids: {map_id_to_initial(employee_list)}")


if __name__ == "__main__":
    main()
