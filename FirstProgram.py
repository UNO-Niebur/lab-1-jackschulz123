#FirstProgram.py
#Name: Jack Schulz
#Date: 1/22/26
#Assignment:Lab 1

def main():
  print("First Program")
  #Say hello
  print("Hello")
  #Ask for the user's name
  print("What is your name?")
  name = input("Enter your name here: ")

  #Use the user's name in the program.
  print("It's a pleasure to meet you",name)

  #Ask the user for their age.
  print("If you don't mind me asking, how old are you?")
  age = int(input("Enter age here:"))

  #Tell the user what year they were born in.
  print("It appears you were born in the year:", 2025 - age)
  #Assume that they have not had their birthday yet this year.


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
