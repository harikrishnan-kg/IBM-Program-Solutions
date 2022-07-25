# WAP to check string is palindrome

str1=input('Enter a string :')
if str1==str1[::-1]:
    print(str1,'is palindrome')
else:
    print(str1,'is not palindrome')
    

# Enter a string :malayalam
# malayalam is palindrome
 
# Enter a string :english
# english is not palindrome

# <----------------------------------------------------->

# WAP to remove particluar character from string

str1=input('Enter a string :')
ch=input('Enter a character :')
str1=str1.replace(ch,'')
print(str1)

# Enter a string :Palindrome
# Enter a character :P
# alindrome

# <----------------------------------------------------->

# WAP to count occurrence of characters in a string

str1=input('Enter a string :')
ch=input('Enter a character :')
count =str1.count(ch)
print('No of occurence of ',ch,': ',count)

# Enter a string :IBMBATCHIBM
# Enter a character :B
# No of occurence of  B :  3

# <----------------------------------------------------->
# WAP to delete the repeating characters in a string

str1=input('Enter a string :')
s=[i for i in str1]
s=set(s)
str1=''.join(s)
print(str1)

 
# Enter a string :ibmbatchb
# iathmcb


# <----------------------------------------------------->

# WAP to find smallest and largest elemt in an Array

list1=list(map(int,input('Enter elements of array :').split()))
print(list1)
print('Smallest element :',min(list1))
print('Largest element :',max(list1))


# Enter elements of array :33 27 32 1 34 100
# [33, 27, 32, 1, 34, 100]
# Smallest element : 1
# Largest element : 100

