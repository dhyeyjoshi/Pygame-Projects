#import turtle
#wn = turtle.Screen()
#wn.bgcolor('pink')
#my_turtle = turtle.Turtle()
#my_turtle.speed(5)
#def square(length,angle):
 #   for i in range(4):
  #      my_turtle.forward(length)
   #     my_turtle.right(angle)
#while True:
 #   square(100,90)
  # my_turtle.right(11)
  
#which letter we want to print
print("hello" [0:2])
print("hello" [0:-1])
print("hello" [-1])
#reverse a string
print("hello" [::-1])
print("olleh" [::-1])
#example
name="dhyey 2608 | 08 | 2000"
print(name)
#index position
print(name.index('|'))
#print that word on that index number
print(name[11])
#range from 0 to | 
data=name[0:name.index('|')]
print(data)
#this is used if two same words are there in strings
print(name.find('|',12))#12 means see '|' after 12th position
print(name[16])
#print in between words so we make a range from '|' to second '|'
print(name[name.find('|')+1:name.find('|',12)])
#exmple 2
race=['john','ram','shyam']
print(race[0])
print(race[1])
print(race[2])
#shortcut to split words into list by using split()
greeting='what are uh doing'.split(' ')
print(greeting)
print(greeting[0])
print(greeting[1])
print(greeting[2])
print(greeting[3])
print(greeting[-1])
print(greeting[::-1])
print(race[::-1])
#same example
details=name.split('|')
print(details)
#giving the names to individual words of list
naam=details[0]
luckynumber=details[1]
birthyear=details[2]
print(naam)
print(luckynumber)
print(birthyear)
#shortcut of upper example is this
naam,luckynumber,birthyear=name.split('|')
print(naam)
print(luckynumber)
print(birthyear)
#using append to add something to the list
numbers=[1,2,3,4,5]
numbers.append(6)
print(numbers)
#shortcut is to add numbers in list just make a loop
for number in range(7,101):#range(start,stop)
    numbers.append(number)
print(numbers)
print(numbers[::-1])
#Dictionaries
#DICT[key]-->value
#LIST[0]--> 0th element of the list
#{key1: value1,key2: value2,.....}
phone_book ={
    'fat':['222-222-2222','fat@fatgmail.com'],
    'bob':['333-333-3333','bob@bobgmail.com'],
    'cat':['456-378-383','cat@catgmail.com'],
    }
print(phone_book['fat'][0])
print(phone_book['fat'][1])
print(phone_book['cat'][1])
#DICT[fat] --> list of things containig #ph and email.


#if (CONDITION --> TRUE):
# THEN THIS

if True:
    print("Hello")

if False:
    print("Hi")

# == , < , > , <= , >= , !=
print(5==5)#-->TRUE
print(5<5)#-->FALSE
print(5>5)#-->FALSE
print(5<=5)#-->TRUE
print(5>=5)#-->TRUE
print(5!=5)#-->FALSE

jonny_hours_worked=40
print(jonny_hours_worked>40)
print(jonny_hours_worked<40)
print(jonny_hours_worked>=40)
print(jonny_hours_worked<=40)
print(jonny_hours_worked==40)
print(jonny_hours_worked!=40)

jonny_hours_worked=41
if jonny_hours_worked>40:
    print("Pay him overtime")
















