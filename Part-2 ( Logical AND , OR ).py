#LOGICAL 'AND'
print(True and False)#-->False
print(False and True)#-->False
print(False and False)#-->False
print(True and True)#-->True
print("-------------------------------------------------------------------")
#LOGICAL 'OR'
print(True or False)#-->True
print(False or True)#-->True
print(False or False)#-->False
print(True or True)#-->True
print("-------------------------------------------------------------------")
#LOGICAL 'NOT'
print(not True)#-->False
print(not False )#-->True
print(not(True or False))#-->False
print(not(True and False))#-->True
print("-------------------------------------------------------------------")
homeworkcompleted=True
cleanedroom=True
if homeworkcompleted and  cleanedroom:
    print("he can play games")
print(not(homeworkcompleted or not(cleanedroom)))
print("-------------------------------------------------------------------")
#Rock , paper and scissor game
human='rock'
computer='scissor'
if human == 'rock' and computer == 'scissor':
    human_score=1
computer = 'bananas'
if human == 'rock' and computer == 'scissor':
    human_score=1
elif human=='rock' and computer== 'bananas':
    human_score=0
    computer_score=0
print("You can't pick anything except rock , paper and scissor")
#if (CONDITION --> True):
#THIS BLOCK OF CODE RUNS
if computer!='rock' or computer!='Scissor' or computer!='Paper':
    print("WRONG CHOICE ,PICK AGAIN")
Computer='rock'
if computer!='rock' or computer!='Scissor' or computer!='Paper':
    print("WRONG CHOICE ,PICK AGAIN")
if computer!='rock' and  computer!='Scissor' and computer!='Paper':
    print("WRONG CHOICE ,PICK AGAIN")
computer='rock'
if computer!='rock' and  computer!='Scissor' and computer!='Paper':
    print("WRONG CHOICE ,PICK AGAIN")
print("----------------------------------------------------------------")
for i in range(5):
    print("Hello")
#print([0,1,2,3,4])
#range(0,2)-->[0,1,2]

#print numbers from 20 to 40
for number in range(20,41):
    print(number)
#[1,2,3]-->6 -->1+2+3=6
count=0
for number in range(1,4):
    #new_count=old_count+number
    count=count+ number
    #it should be 6
    #print(count)
#write the function that sums all the elements of the list
#return count
def sum_list(my_list):
    count=0
    for number in my_list:
        count=count+number

    return count

assert sum_list([1,2,3])== 6
assert sum_list([1,2,3,4])==10
print(sum_list([1,2]))




























