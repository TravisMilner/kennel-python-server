CUSTOMERS = [
    {
      "email": "hello@hello.com",
      "password": "whatsup",
      "name": "Timmy Milner",
      "id": 1
    },
    {
      "email": "trav@trav.com",
      "password": "travis",
      "name": "Travis Milner",
      "id": 2
    }
]


def get_all_customers():
    return CUSTOMERS


def get_single_customer(id):

    requested_customer = None

    for customer in CUSTOMERS:

        if customer["id"] == id:
            requested_customer = customer

    return requested_customer