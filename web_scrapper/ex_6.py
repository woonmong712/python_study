# # password_correct = False

# # if password_correct:
# #     print("Here is your money")
# # else:
# #     print("password is not correct")


# age = int(input(""))

# if age < 18:
#     print("you can't drink")
# elif age >= 18 and age <= 35:
#     print("You drink beer")
# else:
#     print("Go ahead!")
# from random import randint, random

# print("Welcome to Python Casino")
# pc_choice = randint(1,100)
# playing = True

# while playing:
#     user_choice = int(input("Choose number. (1-100) "))
#     if user_choice == pc_choice:
#         print("You won!")
#         playing = False
#     elif user_choice > pc_choice:
#         print("Lower!")
#     elif user_choice < pc_choice:
#         print("Higher!")



# days = ["a","b"]
# days_1 = ("a", "b","c")
# player = {"name" : "woonmong", "age" : 31, "alive" : True, "fav_food" : ["🥘", "🍬"]}
# print(player.get("fav_food"))
# print(player["name"])
# player["fav_food"].append("🍘")
# print(player["fav_food"])

# print(days_1.count("a"))
# print(days_1[-1])


websites = (
    "https://google.com",
    "airbnb.com",
    "twitter.com",
    "facebooks.com",
    "tiktok.com"
)

for website in websites:

    if not website.startswith("https://"):
        website = f"https://{website}"
    print(website)