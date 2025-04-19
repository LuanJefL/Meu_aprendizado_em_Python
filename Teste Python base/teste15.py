A1 = 10
A2 = 0
try:
    print(A1/A2)
except ZeroDivisionError as error:
    print(10/A2)
    print(error)