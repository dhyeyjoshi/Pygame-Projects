"""
@Clever Programmer

Backstory: Usain Bolt, you, and Qazi
had a race. Surprisingly, Usain bolt won.
You came in 2nd and Qazi came in 3rd :(.

Can you think of a way to write a function 
that given a person's name, returns his/her place?

ALSO

Can you think of a way to write a function 
that given a place, returns his/her name?

WRITE 2 FUNCTIONS

One that converts choice to number
and
One that converts number to choice.
"""

# Make sure to un-comment the code test line 
# all the way below when you are done.
# Remember to name your function correctly.
# WRITE YOUR CODE HERE...
def choice_to_number(choice):
    return {'Usain':1,'Me':2,'Qazi':3}[choice]  
  # if number is 1 then return usain bolt.
  
def number_to_choice(number):
    return {1:'Usain',2:'Me',3:'Qazi'}[number]


# DO NOT remove lines below here,
# this is designed to test your code.

def test_choice_to_number():
  assert choice_to_number('Usain') == 1
  assert choice_to_number('Me') == 2
  assert choice_to_number('Qazi') == 3
  
def test_number_to_choice():
  assert number_to_choice(1) == 'Usain'
  assert number_to_choice(2) == 'Me'
  assert number_to_choice(3) == 'Qazi'

  
def test_all():
    test_choice_to_number()
    test_number_to_choice()
    print("Success")

  
# test your code by un-commenting the line(s) below
test_all()

