# Program to convert heights in inches to centimeters

def inches_to_cm(heights_in_inches):
    return [round(height * 2.54, 2) for height in heights_in_inches]

def main():
    heights_in_inches = list(map(float, input("Enter heights in inches separated by spaces: ").split()))

    heights_in_cm = inches_to_cm(heights_in_inches)
    print("Converted heights in centimeters:", heights_in_cm)

if __name__ == "__main__":
    main()
