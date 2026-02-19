class InvalidAgeError(Exception):
    pass


def check():
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            raise InvalidAgeError("Age cannot be zero or negative.")

        if age < 18:
            raise InvalidAgeError("You are not eligible to vote.")

        print("You are eligible to vote!")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

    except InvalidAgeError as e:
        print("Error:", e)

    except Exception as e:
        print("Unexpected error occurred:", e)

    finally:
        print("Age verification completed.")

check()
