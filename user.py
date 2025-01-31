user_info = {}
user_info["What is the user's name?"] = input("What is the user's name?\n")
user_info["What is the user's age?"] = input("What is the user's age?\n")
user_info["What is the user's country of birth?"] = input("What is the user's country of birth?\n")
user_info["What is the user known for?"] = input("What is the user known for?\n")
print("\nUser Information:")
for key, value in user_info.items():
    print(f"{key.capitalize()}: {value}")
