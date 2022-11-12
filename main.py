from random import *
print('''Добро пожаловать в числовую угадайку. 
Введите предел диапазона для случайного выбора числа:''')
limit = int(input())
number = randint(1, limit)
print('Если не сможете угадать, то напишите "сдаюсь". Введите ваше число:')

def is_valid(string):
    if string.isdigit() and 0 <= int(string) <= limit:
        return True
    else:
        return print(f'А может быть все-таки введем целое число от 1 до {limit}?')
    
count = 0    
while True:    
    string = input()   
    if string == 'сдаюсь':
        print(f'''Загаданное число = {number}.
Спасибо, что играли в числовую угадайку. Еще увидимся...''')  
        break
    else:
        if is_valid(string) == True:        
            if int(string) < number:
                count += 1
                print('Ваше число меньше загаданного, попробуйте еще разок') 
            elif int(string) > number:
                count += 1
                print('Ваше число больше загаданного, попробуйте еще разок') 
            elif int(string) == number:
                print(f"""Вы угадали, поздравляем! Кол-во попыток = {count+1}. 
        Желаете продолжить игру? (да/нет)""")
                if input() in ('да', 'yes'):
                    print('Введите новый предел диапазона для случайного выбора числа:')
                    limit = int(input())
                    number = randint(1, limit)
                    print('Введите ваше число:')
                else:
                    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                    break
