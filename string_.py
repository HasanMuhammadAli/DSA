# def summ(nums):
#     n = len(nums)
#     ans = 0
#     for i in range(n):
#         ans += nums[i]
    
#     return ans

# nums = [0, 3, 5]
# print(summ(nums))
    
 
# def largest(nums):
    
#     ans = nums[0]
#     sans = ans
#     for i in nums:
#         if ans < i:
#             sans = ans
#             ans = i
#         elif  i > sans:
#             sans = i
        
#     return ans, sans
    
# nums = [12, 34, 13, 90, 78]
# print(largest(nums))
'''

#1.Write a program that takes two numbers as input and prints their sum.
num1 = int(input("Enter the first number:  "))
num2 = int(input("Enter the second number: "))
print("The sum is : ", num1+num2)

#2.Write a program that takes a string as input and prints its length.
text = input("Enter string:")
print("Length: ",len(text))

#3.Write a program that takes a sentence and then prints the number of words in that sentence.
sentence = input("Enter a sentence: ")
print("Number of words in the sentence: ", sentence.count(' ')+1)

#4.Write a program that takes a string as input and counts the number of uppercase letters in the string.
x = input("Enter a string: ")
upper = 0 
lower = 0 
for i in x:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1
print("Upper: ", upper)
print("Lower: ", lower)

#5.Write a program that takes a sentence and then converts all the characters to uppercase.
sentence = input("Enter a sentence: ")
print(sentence.upper())


#6.Write a program that takes a string as input and replaces all occurrences of the letter ‘a’ with the letter ‘e’.
word = input("Enter a string: ")
rep = word.replace('a', 'e')
print(rep)

#7.Create a program that checks if two given strings are anagrams of each other.
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if sorted(word1.replace(" ","").lower()) == sorted(word2.replace(" ","").lower()):
    print("The given words are anagrams")
else:
    print("The given words are not anagrams")

#8.Create a program that checks if a given string is a palindrome.
word = input("Enter the string: ")

if word.replace(" ","").lower() == word[::-1].replace(" ","").lower():
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")

#9.Create a program that checks if a substring is present in a given string.
word = input("Enter a string: ")
sub = input("Enter the substring to check: ")

if sub in word:
    print("The substring is present in the string")
else:
    print("The substring is not present in the string")

#10.Write a program that reverses the order of words in a given sentence.
sentence = input("Enter a sentence: ")

words = sentence.split(" ")
words.reverse()
newsent = ""

for i in words:
    newsent += i + " "
print(newsent)

#11. Implement a Caesar cipher encryption and decryption program. the key (shift) value of this message is 3.
# The formula of encryption is: En (x) = (x + n) mod 26
message = input("Enter the message:")
result = ""
shift = 3
for char in message:
    if char.isalpha():
        ascii_offset = 65 if char.isupper() else 97
        result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset )
    else:
        result += char
print(result)


#12. Write a program that counts the number of vowels in a given string.
word = input("Enter a text : ")

vowels = 'AEIOUaeiou'
x = 0
count = len([char for char in word if char in vowels])
print(count)

#13. Create a program that converts a given sentence into Pig Latin (move the first letter of each word to the end and add “ay”).
txt = input("Enter a sentence: ")

words = txt.split(" ")
newsent = ""
for i in words:
    newsent += (i[1:] + i[:1]+"ay ")
print(newsent)

#14. Write a program that capitalizes the first letter of each sentence in a given paragraph.
paragraph = input("Enter a paragraph: ")
sentences = paragraph.split('.')
output = ""
for sent in sentences:
    cap = sent.strip().capitalize()
    output += cap + '. '
print(output)

#15. Write a program that finds the longest word in a given sentence.
sentence = input("Enter the sentence: ")
words = sentence.split()
output = max(words, key=len) # key=len “When comparing items, compare them by their length, not alphabetically.”
print("Longest word in the given sentence:", output)

#16. Write a program that reverses the order of words in a given sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()
words.reverse()
rev = " ".join(words)
print(rev)

#17. Given a list of strings, write a program to find all pairs of strings that are palindromes.
strings = ["race", "car", "rat", "tar","rac"]
rev = ""
palindrome = []
for s in strings:
    rev = s[::-1]
    if rev in strings and rev not in palindrome:
        palindrome.append(s)
        print(s+" and "+ rev+" are palindrome.")


#18. Given three strings, write a program to check if the third string can be formed by interleaving the characters of the first two strings.
s1 = "blue"
s2 = "berry"
s3 = "bbeluerry"

if sorted(s3) == sorted(s1+s2):
    print("The third word is interleaving the characters of the first two words.")
else:
    print("The third word is not interleaving the characters of the first two strings.")

'''

#19. Write a program to find all permutations of a smaller string within a larger string.
#Later 

#20. Create a program that performs basic string compression using the counts of repeated characters. For example, the string “aabcccccaaa” would become “a2b1c5a3”.
string = "aabcccccaaa"
# count = 0
# ans = []
# i = 0
# flag=False
# for s in string:
#     if i == 0 and not flag:
#         ans.append(s)
#         flag=True

#     if s is ans[i]:
#         count += 1
#     elif s is not ans[i]:
#         ans.append(count)
#         count = 1
#         ans.append(s)
#         i += 1
# print(ans)


count = 1
ans = []
i = 0 
flag = True

for s in string:
    if i == 0 and flag:
        ans.append(s)
        flag = False
        continue

    if s is ans[i]:
        count += 1
    
    elif s is not ans[i]:
        ans.append(count)
        i += 1
        ans.append(s)
        count = 1
        i += 1
ans.append(count)
print(ans)