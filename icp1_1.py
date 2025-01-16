# Program to Get Full Name and Alternate Characters
def fullname(first_name, last_name):
    return f"{first_name} {last_name}"

def string_alternative(input_string):
    return input_string[::2]

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    full_name = fullname(first_name, last_name)
    print(f"Full Name: {full_name}")

    alternative_string = string_alternative(full_name)
    print(f"String with alternate characters: {alternative_string}")

if __name__ == "__main__":
    main()
