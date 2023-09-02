import time
import random
def game():
    use = input("would you like to start? say yes")
    if use == 'yes' :
        user=int(input('enter a number in between 1 to 100: '))
        comp=int(random.uniform(0,101))
        while comp!=user:
            if comp>user:
                print('given number is less than the answer')
                a=int(input('enter another number: '))
                user=a 
            else :
                print('given number is greater then tne answer')
                a=int(input('enter another number: '))
                user=a
        else :
            print(f'yeah! the answer is {user}')
        time.sleep(2)
        game()
game()    
