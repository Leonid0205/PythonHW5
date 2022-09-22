# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

# text_str = 'абвгдейка - это передача'
# delete_fragment = 'абв'
# print(text_str)
# def text_delete_fragment(s: str, delete_fragment: str):
#     '''Функция удаляет слово из строки, если сторока содержит фрагмент'''
#     if delete_fragment not in s:
#         print('There is no such fragment in the text')
#         return False
#     s = s.split()
#     result = ''
#     delete_fragment = 'абв'
#     for i in range(len(s)):
#         if len(s[i]) >= len(delete_fragment):
#             if not delete_fragment in s[i]:
#                 result = result + s[i] + ' '
#         else:
#             result = result + s[i] + ' '
#     return result
# print(text_delete_fragment(text_str, delete_fragment))

# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]

# list_of_languages = 'Python Java C C++ JavaScript C# R Go HTML Swift Pascal Delphi'
# print()
# print(f'Initial text: {list_of_languages}')
# print()
# def create_list_of_tuples(s: str):
#     '''Функция возвращает список кортежей'''
#     s = s.upper().split()
#     result = list(enumerate(s, start=1))
#     return result
# def filter_list_of_tuples(s: list):
#     '''Функция фильтрует список кортежей'''
#     l = [list(i) for i in s]
#     res1 = []
#     res2 = []
#     for i in range(len(l)):
#         for j in reversed(range(len(l[i]) - 1)):
#             sum = 0
#             for k in range(len(l[i][1])):
#                 sum = sum + ord(l[i][1][k])
#             if sum % l[i][0] == 0 & j == 0:
#                 res1.append(sum)
#                 res2.append(l[i][1])
#     result2 = [(x, y) for x, y in zip(res1, res2)]
#     return result2
# tup_languages = create_list_of_tuples(list_of_languages)
# filtred_list_of_tuples = filter_list_of_tuples(tup_languages)
# print(f"Filtred list of tuples is: {filtred_list_of_tuples}")

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# 1. ИГРА С ДРУГИМ ИГРОКОМ

# import random

# def first_turn():
#     player = ''
#     player1 = ''
#     flip = random.randint(1, 3)
#     if flip == 1:
#         print('It is first players turn!')
#         player = 'Player 1'
#         player1 = 'Player 2'
#     else:
#         print('It is second players turn!')
#         player = 'Player 2'
#         player1 = 'Player 1'
#     return player, player1
# players = first_turn() 
# while True:    
#     try:
#         turn_limit = int(input('Input the limit of candies for player per turn: '))
#         if 0 < turn_limit:
#             break
#         else:    
#             print('The number needs to be positive and not 0!!! ')
#     except ValueError:
#         print('ValueError!')
# while True:   
#     try:
#         result3 = int(input('Input the total amount of candies: '))
#         if 0 < result3 & result3 > turn_limit:
#             break
#         else:    
#             print('The number needs to be more than limit and above zero!!! ')
#     except ValueError:
#         print('ValueError!')

# if result3 > turn_limit:
#     while result3 > turn_limit:
#         try:
#             turn = int(input(f'{players[0]} choose a number between 1 and {turn_limit}: '))
#             if 0 < turn < turn_limit:
#                 result3 = result3 - turn
#                 print(result3)
#             else:    
#                 print(f'{players[0]} the number needs to be between 1 and {turn_limit} npt negative or zero!!! ')
#         except ValueError:
#             print('Invalid value!')
#         if result3 <= 1:
#            print(f'{players[0]} You won!!!')
#            break     
#         try:    
#             turn = int(input(f'{players[1]} choose a number between 1 and {turn_limit}: '))
#             if 0 < turn < turn_limit:
#                 result3 = result3 - turn
#                 print(result3)
#             else:
#                 print(f'{players[1]} the number needs to be between 1 and {turn_limit} not negative or zero!!! ')
#         except ValueError:
#             print('Invalid value!')
#         if result3 <= 1:
#            print(f'{players[1]} You won!!!')
#            break     
# if result3 <= turn_limit:
#     while result3 > 1:
#         try:
#             turn = int(input(f'{players[0]} choose a number between 1 and {result3}: '))
#             if 0 < turn <= result3:
#                 result3 = result3 - turn
#                 print(result3)
#             else:    
#                 print(f'{players[0]} the number needs to be between 1 and {result3} npt negative or zero!!! ')
#         except ValueError:
#             print('Invalid value!')
#         if result3 <= 1:
#            print(f'{players[0]} You won!!!')
#            break     
#         try:    
#             turn = int(input(f'{players[1]} choose a number between 1 and {result3}: '))
#             if 0 < turn <= result3:
#                 result3 = result3 - turn
#                 print(result3)
#             else:
#                 print(f'{players[1]} the number needs to be between 1 and {result3} npt negative or zero!!! ')
#         except ValueError:
#             print('Invalid value!')
#         if result3 <= 1:
#            print(f'{players[1]} You won!!!')
#            break     

# 2. ИГРА С БОТОМ

# import random

# def first_turn():
#     player = ''
#     player1 = ''
#     flip = random.randint(1, 3)
#     if flip == 1:
#         print('It is players turn!')
#         player = 'Player'
#         player1 = 'Bot'
#     else:
#         print('It is bots turn!')
#         player = 'Bot'
#         player1 = 'Player '
#     return player, player1
# players = list(first_turn())
# print(players)

# while True:    
#     try:
#         turn_limit = int(input('Input the limit of candies for player per turn: '))
#         if 0 < turn_limit:
#             break
#         else:    
#             print('The number needs to be positive and not 0!!! ')
#     except ValueError:
#         print('ValueError!')
# while True:   
#     try:
#         result3 = int(input('Input the total amount of candies: '))
#         if 0 < result3 & result3 > turn_limit:
#             break
#         else:    
#             print('The number needs to be more than limit and above zero!!! ')
#     except ValueError:
#         print('ValueError!')

# def turn_player(result3, turn_limit):
#     while True:
#         try:
#             turn = int(input(f'{players[0]} choose a number between 1 and {turn_limit}: '))
#             if 0 < turn <= turn_limit:
#                 break
#             else:    
#                 print(f'{players[0]} the number needs to be between 1 and {turn_limit} not negative or zero!!! ')
#         except ValueError:
#             print('Invalid value!')
#     result3 = result3 - turn
#     print(f'Player took {turn} candies')
#     print(f'The amout of candies left is: {result3}')
#     return(result3)
        
# def tur_bot(result3, turn_limit):
#     turn_bot = (result3 - 1)%(turn_limit + 1)
#     result3 = result3 - turn_bot
#     print(f'Bot took {turn_bot} candies')
#     print(f'The amout of candies left is: {result3}')
#     return result3

# if result3 > turn_limit:
#     while result3 > turn_limit:
#         if players[0] == 'Player':
#             result3 = turn_player(result3, turn_limit)
#             players[0] = 'Bot'
#         else: 
#             result3 = tur_bot(result3, turn_limit)
#             players[0] = 'Player'
# if result3 <= turn_limit:
#     while result3 > 0:
#         turn_limit = result3
#         if players[0] == 'Player':
#             result3 = turn_player(result3, turn_limit)
#             players[0] = 'Bot'
#         else: 
#             result3 = tur_bot(result3, turn_limit)
#             players[0] = 'Player'
#     if players[0] == 'Player':
#         print('Player wins!')
#     else:
#         print('Bot wins!')