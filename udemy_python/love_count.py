# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
combined_String = name1 + name2
lower_case_string = combined_String.lower()

true = ['t', 'r', 'u', 'e']
love = ['l', 'o', 'v', 'e']


def CountLetter(lower_case_string, compareList):
    cnt = 0
    for name in lower_case_string:
        for letter in compareList:
            if letter == name:
                cnt += 1
    return cnt


true_count = CountLetter(lower_case_string, true)
love_count = CountLetter(lower_case_string, love)
love_score = int(str(true_count) + str(love_count))

if (love_score < 10) or (love_score > 90):
    print(
        f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score},you are alright together")
else:
    print(f"Your score is {love_score}.")
