numbers = [1,2,3,4,5,6]

def sum(all_numbers):
    total = 0
    for n in all_numbers:
        total += n
    return total

number = sum(numbers)
print(number)