# ---------- Q1-----------

import math
from msilib.schema import Directory

print(">>>>>>>>>>>>>>>>>Q1<<<<<<<<<<<<<<<<<<<<\n")


def word_count(s):  # making function
    counts = {}  # making empty dictionary
    arr_1 = s.split()  # splitting input in  arr_1

    for word in arr_1:  # making loop for word count
        if word in counts:  # if find word then add 1
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1  # if not find then remain 1

    return counts  # return counts


arr_2 = str(input("Enter your string \n"))  # taking input
arr_2 = arr_2.upper()  # making upper case letter
arr_3 = arr_2.split()  # splitting  arr_2
dic1 = {}  # making new dict for taking user input
if arr_3.__len__() == 1:  # checking if it is single word
    for keys in arr_2:  # loop for making all checking characters repeatation
        dic1[keys] = dic1.get(keys, 0) + 1  # adding plus one if repeat
    # printing count result of dict or characters repeatition
    print("Counting of all characters is : " + str(dic1))
else:  # for no. of words checking
    print(word_count(arr_2))  # for printing no. of word repeating in sentence


print("------------------++++-------------------------------")


# -----------------Q2-----------------------

# Taking year input from user
print(">>>>>>>>>>>>>>>>>Q2<<<<<<<<<<<<<<<<<<<<\n")
year = int(input("Enter the year: \n"))
# Checking for leap year
if (year % 400 == 0) and (year % 100 == 0):
    leap_year = True
elif (year % 4 == 0) and (year % 100 != 0):
    leap_year = True
else:
    leap_year = False

# Taking Month input from user
month = int(input("Enter the month [1-12]: \n"))

# Checking for 30 day's month and 28 day's and 29 day's of february
if month in (1, 3, 5, 7, 8, 10, 12):  # for 31 day's months checking
    month_length = 31
elif month == 2:  # for february month checking of leap year
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:  # for exception from above months
    month_length = 30

# Taking input day from user
day = int(input("Enter the day [1-31]: \n"))

# checking for new year date

if day < month_length:  # for checking of last day
    day = day+1
else:
    day = 1
    if month == 12:
        month = 1
        year = year + 1  # increament for new year
    else:
        month = month + 1  # icreament for new month
 # printing the next day
print("The next date is [dd-mm-yyyy] :::: %d-%d-%d." % (day, month, year))
print("------------------++++-------------------------------")


# ----------------Q3---------------------
# making tuple list
print(">>>>>>>>>>>>>>>>>Q3<<<<<<<<<<<<<<<<<<<<\n")
mylist = [2, 4, 7, 10, 11, 25]
print("My list is")
print(mylist)  # printing it


# squaring the number of list and printing with its previous input
print("My squaring tuple list is :")

# making new tuple list of square of ols tuple list
myresult = [(num, pow(num, 2)) for num in mylist]
print(myresult)  # printing new tuple list
print("------------------++++--------------------------------------")


# -------------------Q4-----------------
print(">>>>>>>>>>>>>>>>>Q4<<<<<<<<<<<<<<<<<<<<\n")


def point():
    marks = float(input("Enter Grade Point: \n"))
    # check if marks in the range of conditions
    if marks > 10 or marks < 4:
        print("Error==>Wrong input")
        marks = point()
    return marks


# changing float value into integer if enter by user
grade = math.floor(point())


# checking which situation grade will fall and printting with respect to its marks
if (grade == 10):
    print("Your grade is A+ and Outstanding Performance")
elif(grade == 9):
    print("Your grade is A and Excellent Performance")
elif(grade == 8):
    print("Your grade is B+ and Very Good Performance")
elif(grade == 7):
    print("Your grade is B and Good Performance")
elif(grade == 6):
    print("Your grade is C+ and Average Performance")
elif(grade == 5):
    print("Your grade is C and Below Average Performance")
elif(grade == 4):
    print("Your grade is D and Poor Performance")
else:
    print("Error ==>> Wrong Input")

print("------------------++++--------------------------------------")

print("------------------++++--------------------------------------")

# -----------------------Q5------------------------
print(">>>>>>>>>>>>>>>>>Q5<<<<<<<<<<<<<<<<<<<<\n")
# no. of rows we going to print
num_rows = 6

for num_2 in range(num_rows):
    # printing spaces
    for num_3 in range(num_2+5):  # for making spaces as program printing its characters
        print(' ', end='')  # printing alphabet

    # for printing character two character less then previous characters
    for num_3 in range(2*(num_rows-num_2)-1):
        print(chr(65 + num_3), end='')
    print()

print("------------------++++++--------------------------------------")


# ----------------- Q6 ----------------------
print(">>>>>>>>>>>>>>>>>Q6<<<<<<<<<<<<<<<<<<<<\n")
class_list = dict()  # making empty dict
ask_1 = int(input("Enter your SID\n"))  # taking input of key
ask_2 = input("Enter your name\n")  # taking input of value
class_list[ask_1] = [ask_2]  # making dict of key and value pair
while True:  # loop of running this loop n times user want

    ask_123 = input(
        "If you want us to ask your SID again then enter'Y' and for not again enter'N' \n")
    # taking input for again asking sid and name
    if ask_123 == 'Y':
        ask_1 = int(input("Enter your SID\n"))
        ask_2 = input("Enter your name\n")
        class_list[ask_1] = [ask_2]
    elif ask_123 == 'N':  # for breaking if loop and not asking sid and name
        break
    else:
        print("Error==>Invalid input")  # if enter invalid input


# a) part:------
print("a) part:------")
print("List of SID with name")
print(class_list)  # printing sid and name dict

# b) part:------
print("\n")
print("b) part:------")
print("Sorted by student name")
# sorted by name and printing it
print(sorted(class_list.items(), key=lambda kv: (kv[1], kv[0])))


# c) part: ------
print("\n")
print("c) part: ------")
print("Sorted by SID")
class_list2 = sorted(class_list.items())  # sorted by sid
print(class_list2)  # printing that sort by sid
# d) part:---
print("\n")
print("d) part:---")
# searching name by sid asking to user
key_2 = input("Enter Y to search name by SID and 'N for not searching'\n")
if key_2 == 'Y':
    key = int(input("Enter SID you want to find\n"))  # taking sid by user
    if key in class_list:  # searching sid in dict
        print('The name is:', class_list[key])  # printing user name
    else:
        print('That key is not in the dictionary.')  # print for not found name
elif key_2 == 'N':
    print("You are out of terminal")

else:
    print("Error==>Invalid input")

print("------------------++++++--------------------------------------")


# --------------------Q7-------------------
# Function for nth Fibonacci Sequence
print(">>>>>>>>>>>>>>>>>Q7<<<<<<<<<<<<<<<<<<<<\n")
num_1 = int(input("Enter the number to find its Fibonacci series\n"))
print("Fibonacci sequence given below")


def Fibonacci(n):
    if n <= 1:  # for -ve ,0 and 1 number returnning n
        return n
    else:  # for greater than 1 returnning fibonnaci sequence with or formula applied
        return Fibonacci((n)-1)+Fibonacci((n)-2)


if num_1 <= 0:
    # detecting -ve and 0 value enter by user
    print("Error==> Invalid input")
else:

    sum = 0
    # initializing sum equal to zero
    for i in range(num_1):
        # i for no of sequnce and num_1 is value where the code will run
        print(Fibonacci(i))  # printting all fibonnacci no according to its i
        # summing with 0 and new no of fibonnacci sequence
        sum = sum + Fibonacci(i)
Average = (sum / num_1)
print("Average value of Fibonacci series")
# for 0ne decimal no. output we using it
Average_value = math.floor(Average*10)/10
print(Average_value)
print("------------------++++++--------------------------------------")


# ----------------------Q8---------------------
print(">>>>>>>>>>>>>>>>>Q8<<<<<<<<<<<<<<<<<<<<\n")
# making set as given in question
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# a) part:----
print("a) part:----")
# making union of set1 and set2
a_partset = ((Set1 | Set2)-(Set1 & Set2))
print(a_partset)
# b) part:----
print("b) part:----")
# Subtracting intersection of sets taking two at a time from the union of all three sets
b_partset = ((Set1 | Set2 | Set3)-(Set1 & Set2)-(Set2 & Set3) - (Set3 & Set1))
print(b_partset)
# c) part:----
# Making sum of common element from taking two set at a time out of three set
print("c) part:----")
c_partset = ((Set1 & Set2) | (Set2 & Set3) | (Set3 & Set1))
print(c_partset)
# d) part:----
# making range set for d) and e) part of question
range = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("d) part:----")
d_partset = ((range)-Set1)
# subtrating set1 from range
print(d_partset)
# e) part:----
print("e) part:----")
# subtrating union of all three set from range
e_partset = ((range)-(Set1 | Set2 | Set3))
print(e_partset)
print("------------------++++++--------------------------------------")
