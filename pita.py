import random
import time

def pick_random_number():
    return random.randint(1, 30)


def celebratory_message(number):
    return f"Congratulations!  YOU WON!!!!!: {number}!"

if __name__ == "__main__":
    for _ in range(1):  
        
        random_number = pick_random_number()
        
        print('And the winner isssssssssssssssss:')
        time.sleep(10)
        message = celebratory_message(random_number)
        print(message)
