import random

random_number = random.randint(1, 10)

steps = 6

while True:
    steps -= 1

    print(f"Step {steps}:")
    try:
        direction = int(input('input my number: '))
        if direction == random_number:
            print('Congratulations! You won!')
            print(random_number)
            break
    
    except NameError:
        print("please enter a natural number and do not enter a string or something else.")
        break
    
    except ValueError:
        print("please enter a natural number and do not enter a string or something else.")
        break

    if steps == 1:
        print(f'the {random_number} is my number')
        break
    
    


