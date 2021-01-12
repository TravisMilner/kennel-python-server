EMPLOYEES = [
    {
      "name": "Tommy",
      "locationId": 1,
      "animalId": 4,
      "id": 1
    },
    {
      "name": "Timmy",
      "locationId": 1,
      "animalId": 5,
      "id": 2
    },
    {
      "name": "Tammy",
      "locationId": 1,
      "animalId": 4,
      "id": 3
    }
]


def get_all_employees():
    return EMPLOYEES



def get_single_employee(id):

    requested_employee = None


    for employee in EMPLOYEES:

        if employee["id"] == id:
            requested_employee = employee

    return requested_employee