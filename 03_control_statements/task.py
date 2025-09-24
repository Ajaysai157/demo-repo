import random

def generate_otp():
    return random.randint(1000, 9999)

def get_user_input():
    while True:
        try:
            return int(input("Please enter the OTP: "))
        except ValueError:
            print("Invalid input. Please enter a 4-digit number.")

def main():
    otp = generate_otp()
    max_attempts = 3
    print(f"Your OTP is: {otp}")
    for attempt in range(1, max_attempts + 1):
        user_input = get_user_input()
        if user_input == otp:
            print("You entered the correct OTP!")
            break
        else:
            print(f"Incorrect OTP. Attempts left: {max_attempts - attempt}")
    else:
        print("\nYou have reached the maximum number of attempts.")

if __name__ == "__main__":
    main()
