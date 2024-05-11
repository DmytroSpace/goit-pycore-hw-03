import random

def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> list[int]:

    min_number = max(min_number, 1)             # minimum of min_number and 1
    max_number = min(max_number, 1000)          # maximum of max_number and 1000
    
    numbers = random.sample(range(min_number, max_number + 1), quantity)
    return numbers

lottery_numbers = get_numbers_ticket(1, 36, 5)

print("Ваші лотерейні числа:", sorted(lottery_numbers))
