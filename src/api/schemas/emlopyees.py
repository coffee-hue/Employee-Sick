from typing import List
import strawberry

@strawberry.type
class Sick_Dates:
    dates: str
    
def sick_dates(root):
    return Sick_Dates(
        dates = "11/10/2022"
    )

@strawberry.type
class Employee:
    id: int
    name: str
    position: str
    sick_days: int
    allowed_sick_days: int
    mental_health_days: int
    days_worked_this_year: int
    sick_dates: list["Sick_Dates"]

def Employee_data(root):
    return Employee(
        id = 0,
        name = "Shannon",
        position = "HR",
        sick_days = 5,
        allowed_sick_days = 6,
        mental_health_days = 10,
        days_worked_this_year = 200
    )

@strawberry.type
class Query:
    employee: Employee = strawberry.field(resolver = Employee_data)