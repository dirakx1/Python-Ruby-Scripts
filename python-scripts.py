##Python 

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first == 'a':
        new_word = word + pyg
        print new_word
        
    elif first == 'e':
        new_word = word + pyg
        print new_word
    elif first == 'i':
        new_word = word + pyg
        print new_word
    elif first == 'o':
        new_word = word + pyg
        print new_word
    elif first == 'u':
        new_word = word + pyg
        print new_word
    else:
        new_word = word[1:] + word[0] + pyg
        print new_word
        
    
      
else:
    print 'error'
 

ef hotel_cost(nights):
    return nights * 140

bill = hotel_cost(5)

def add_monthly_interest(balance):
    return balance * (1 + (0.15 / 12))

def make_payment(balance, payment):
    owe = abs (balance - payment)
    y = add_monthly_interest(owe)
    return y
    
new_bill = make_payment(bill, bill/2)
x = make_payment(new_bill, 100)
print x 



inventory = {'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
# Here the dictionary access expression takes the place of a list name 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inv = inventory['backpack']
inv.remove("dagger")
inventory['gold'] = 550

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!

lst = []
def  average(lst):
    suma = sum(lst)
    avr = float(suma) / len(lst)
    return avr


number = 5

def my_function(x):
    return x * 3

print my_function(number)

def list_function(x):
    return x

n = [3, 5, 7]
print list_function(n)

def list_function(x):
    return x[1]

n = [3, 5, 7]
print list_function(n)

def list_function(x):
    x[1]= x[1] +3
    return x

n = [3, 5, 7]
print list_function(n)


file output:

my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(*lsts):
    nlst=[]
    for i in lsts:
        for j in i:
            nlst+=j
    return nlst

print flatten(n)


board = []

def print_board(board):
    for i in range(0,5):
        board = board.append(["O"]*5)
    for x in board:
        print x

board = []

def print_board(board):
    for i in range(0,5):
        board = board.append(["O"]*5)
    for row in board:
        separator.join(row)
        print " ".join(row)

from random import randint 

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

# Add your code below!
def random_row (board):
    for row in board:
        x = len(row) -1
        y = randint(0, x)
        return y
        
def random_col (board):
    for item in board:
        w = len(board[0]) -1
        z = randint(0, w)
        return z

# battleship game

from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print ship_row
print ship_col


if ship_row == guess_row and ship_col == guess_col:
    print "Congratulations! You sank my battleship!"

else:
    print "You missed my battleship!"
    board[int(guess_row)][int(guess_col)] = "X"
    print_board(board)
    if guess_row < 0 or guess_row > len(board) -1 or guess_col < 0 or guess_col > len(board[0]) - 1:
        print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
        print "You guessed that one already."
     
## Battle ship funcionando

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(4): 
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
    break

else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
        
if turn == 3:
    print "Game Over"
    
 

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         

def scrabble_score(word):
    final=0
    if word=='':
        return 0
    else:
        for c in word:
            final+=score[c.lower()]
      
        return final


def censor(text, word):
    word_list = text.split()
    for index in range(len(word_list)):
        if word_list[index] == word:
            word_list[index] = "*"*len(word)
    return " ".join(word_list)



def product(lst):
    total = 1
    for i in lst:
        total *= i
    return total

def remove_duplicates(x):
    new_list = []
    for i in x:
        if i not in new_list:
            new_list += [i]
    return new_list


def median(lst):
    lst = sorted(lst)
    if len(lst) % 2 == 0:
        val1 = lst[(len(lst) / 2) - 1]
        val2 = lst[(len(lst) / 2)]
        return (val1 + val2) / 2.0
    else:
        return lst[(len(lst) / 2)]




import math

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

def grades_variance(scores, average):
    variance = 0
    for i in scores:
        diff = average - i
        square = diff ** 2
        variance += square
    fvariance = variance/len(scores)
    return fvariance

def grades_std_deviation(fvariance):
    return math.sqrt(fvariance)
        
print grades_std_deviation(grades_variance(grades, grades_average(grades)))    

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades, average)
print grades_std_deviation(grades_variance(grades, grades_average(grades))) 
       
      
even_squares = [x**2 for x in range (1, 11) if (x **2)%2 == 0]


## lists

to_21 = range(1, 22)
odds = to_21[::2]
middle_third = to_21[7:14:1]



## Lamdas as defs

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)


squares = [x**2 for x in range(1, 11)]
print filter(lambda x : x >= 30 and x <= 70, squares)

movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}

print movies.items()


threes_and_fives = [x for x in range(1, 16) if x%3 == 0 or x %5 ==0]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != "X"  , garbled)
print message

## manage of multiples prints a string for 3 and 5 multiples, else prints the number

for i in range(1,101):
     if i%3 == 0:
         print "kevin"
     elif i%5 == 0:
         print "bacon"
     elif i%15 == 0 :
         print "Kevin Bacon"
     else:
         print i


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' codigo en python para solucionar el problema:
Bouncy numbers
==============

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''


def bouncy(num): #funcion bouncy
    increment = False
    decrement = False
    n = str(num)
    for d in range(1, len(n)):
        if int(n[d]) > int(n[d - 1]):
            increment = True   #retorna numeros incrementales
        elif int(n[d]) < int(n[d - 1]):
            decrement = True   #retorna numeros decrementales

        if increment and decrement:  #retorna solo numeros bouncy
            return True

    return False

def find():
    i = 1
    b = 0
    p = 0.0
    while True:
        if bouncy(i):
            b+= 1  #contador de numeros bouncy

        p = (b / i)
        if p >= .99:  #hallando porcentaje deseado 99%
            print(i)  #imprimiendo porcentaje
            return(i)
        i += 1
find() #llamando funcion que encuentra porcentaje

#utilizando api de wepay
# download the Python SDK at https://github.com/wepay/Python-SDK o pipi install wepay
from wepay import WePay
wepay = WePay()
wepay = WePay(production=False,access_token='STAGE_df1684a1c7b91f0de51b72e5890891b92d34e47fb3cb48d4dbd8d2a89fa253cc')
response = wepay.call('/preapproval/create', {
	'account_id': 161624111,
	'period': 'monthly',
	'end_time': '2013-12-25',
	'amount': '19.99',
	'short_description': 'A subscription to our magazine.',
	'redirect_uri': 'http://example.com/success/',
	'auto_recur': True
})

print response

# redirect user to response['checkout_uri']

## imap testing 

import imaplib
email = imaplib.IMAP4_SSL('service.service.com')
email.login('mail@mail.com','passwd')
email.logout()


