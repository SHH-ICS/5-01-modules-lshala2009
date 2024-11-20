# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.

print('You have been given 2 random numbers, calculate the sum')
print('-------------------------------------------------------')
import random
num= random.randint(0,100)
print(num)

num = random.randint(0,100)
print(num)
print('What is the sum?' )
print('-----------------')
input()
if num + num: 
    print('correct!')
else: 
  print('incorrect, try again!')
     
  