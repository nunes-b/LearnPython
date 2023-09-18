AGE = 18
USER = (input("What's your name? "))
age_of_user = int(input("Please confirm your age: "))


if (age_of_user >= AGE):
    print(f"Welcome!{USER} you're qualified to have a driver's license. ")
    print(f"You are {age_of_user} yo!")

if (age_of_user < AGE):
    print(
        f"Oh! oops... {USER}, let me tell you some bad news... you still can't have a driver's license, return when you are {AGE} yo!.")
