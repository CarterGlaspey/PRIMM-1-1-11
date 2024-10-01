"""
PRIMM: 1+1 = 11
Description of program here
Name - Date
"""

def main():
  #allows the user to enter a number and then another number which the program adds
    num1: int = int(input("Enter a number: "))
    num2: int = int(input("Enter another number: "))
    total: int = num1+num2

    print(f"{num1} + {num2} = {total}")

if __name__ == "__main__":
  main()
