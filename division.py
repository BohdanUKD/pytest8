
first = 10
second = 5
third = 0

def devision(first_number, secon_number):
    if (first_number / secon_number == 0):
        return "error"
    else:
        return first_number / secon_number

print(devision(first, second))
print(devision(third, second))