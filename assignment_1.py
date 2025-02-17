

count = 0
divisible_numbers = []

for num in range(1,1000):
	if num % 7 == 0 and num % 11== 0:
		count += 1
		divisible_numbers.append(num)

print(f'Numbers between 1 and 1000 that are divided by 7 and 11:  {count}')
print(f'Divisible numbers are: {divisible_numbers}')

#--------------------------------------------------#
def armstrong_num(num):
	digits = str(num)
	num_digits = len(digits)

	sum_of_power = sum(int(digit) ** num_digits for digit in digits)
	return sum_of_power == num

number = int(input("please enter your number:"))
if armstrong_num(number):
	print(f'{number}is armstrong')

else:
	print(f'{number} is not armstrong')

######################################################################################################
def is_armstrong_number(num):
    #Convert the number to a string to easily iterate over digits
    digits = str(num)
    num_digits = len(digits)

    # Calculate the sum of the digits raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)

    # Check if the sum of powers is equal to the original number
    return sum_of_powers == num


# Input from the user
number = int(input('Enter a number: '))

# Check if the number is an Armstrong number
if is_armstrong_number(number):
    print(f'{number} is an Armstrong number.')
else:
    print(f'{number} is not an Armstrong number.')



####################################################
# Create a dictionary where the  keys are numbers from 1 to 5 and the values are the squares of the key\
# Output (1:1, 2:4, 3:9, 4:16, 5:25)
squares_dic = {i: i**2 for i in  range(1,6)}
print(squares_dic)
squares_dic = {}
for i in range(1,6):
    square = i ** 2
    squares_dic[i] = square

print(squares_dic)
def set_isdisjoint(set1, set2):
    return set1.isdisjoint(set2)

set1 = {'Indlovu', 'Inyathi','Idube','Indlulamithi'}
set2 = {'Imoto','indlu','Ibhayisikili','Isihlahla'}
set3 = {'inja','2', '11', 'Indlovu'}
print(set_isdisjoint(set1, set2))
print(set_isdisjoint(set1, set3))

########################################################################################

'''Write a program to find all the vowels present in the sentence 'Python programming is fun' using set.
what are Vowels.
Vowels are letters in the alphabet tha are pronounced without any obstruction allowing the sound to flow freely\
    in the english  language the vowels are A,E,I,O,U
    '''

def find_vowels(sent):
    return set(char for char in sent.lower() if char in 'aeiou')

sent = 'Python programming is fun'
print(find_vowels(sent))


#################################################################################
#Write a program to check if a list is sorted in either ascending or descending or and return True if is sorted.
def is_sorted(lst):
    if lst == sorted(lst):
        return  True
    elif lst == sorted(lst, reverse= True):
        return True
    else:
        return False

lst1 = [1,2,3,4,5]
lst2 = [5,4,3,2,1]
lst3 = [1,4,2,3,5]

print(is_sorted(lst1))
print(is_sorted(lst2))
print(is_sorted(lst3))

###################################################################

# Write a program  that takes two strings and checks if one string is subsequence of the
# other Example: 'abc' is a subsequence of  'aabbcc'.

def is_subsequence(sub1, sub2):
    p1 = 0
    p2 = 0
    while p1 < len(sub1) and p2 < len(sub2):
        if sub1[p1] == sub2[p2]:
            p1 += 1
        p2 += 1
    return p1 == len(sub1)


string1 = "abc"
string2 = "bccb"

if is_subsequence(string1, string2):
    print(f'"{string1}" is a subsequence of "{string2}".')
else:
    print(f'"{string1}" is not subsequence of "{string2}"')

##########################################################
# Create a program that removes the second occurrence of a value from the list example: input
# [1,2,3,2,4] Value 2
# Output [1,2,3,4]

def remove_second_occurrence(lst,value):
    count = 0
    for i in range(len(lst)):
        if lst[i] == value:
            count += 1
            if count == 2:
                del lst[i]
                break
    return lst

# input_list = [1,2,3,2,4]
# value_to_remove = 2
input_list = ['Elephant','Goat','Cow','donkey','Elephant']
value_to_remove = 'Elephant'
output_list = remove_second_occurrence(input_list,value_to_remove)
print(output_list)

