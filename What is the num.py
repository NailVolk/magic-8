import random
num = random.randint(1, 100)
def random_numbers():
    gamer=input()
    count=1
    while gamer!= str(num):
        if gamer.isdigit() != True or (1>int(gamer) or int(gamer)>100):
            print ('А может все-таки введем целое число от 1 до 100?')
            count+=1
            gamer=input()
        elif int(gamer) > num:
            print('Слишком много, попробуй еще раз!')
            count+=1
            gamer=input()
        elif int(gamer) < num:
            print('Слишком мало, попробуй еще раз!')
            count+=1
            gamer=input()
    print('Вы угадали c', count, 'попытки! Поздравляю!')
    print ('Спасибо, что играли в числовую угадайку! Еще увидимся')
print ('Введи целое число от 1 до 100')
random_numbers()
print()