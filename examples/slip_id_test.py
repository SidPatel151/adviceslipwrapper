from client import Client

test = Client()

result = int(input("enter any number, make sure not to enter too high or no slip will form: "))

result = result if result else 1

test.get_id(result)