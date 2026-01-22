#MadLib.py
#Name: Jack Schulz
#Date: 1/22/26
#Assignment: Lab 1

def main():
  print("Madlib:")
  #Ask user for words
  firstadj = input("Give me an adjective to describe someone: ")
  animal = input("Give me any animal: ")
  color = input("Give me any color: ")
  vehicle = input("Give me any vehicle: ")
  place = input("Give me any place in the world: ")
  secondanimal = input("Give me a different animal than the one before: ")
  hours = input("Give me a number 1-100: ")
  stuckin = input("Give me a biome (desert, rainforest, etc.): ")
  hourstwo = input("Give me a number that's smaller than the previous one: ")
  secondadj = input("Give me another adjective to describe someone: ")



  #Print the story with the user supplied words.
  print("The", firstadj, animal, "took a", color, vehicle, "all the way to", place, "without ever sleeping. Along the way, the", animal, "picked up his friend who is a", secondanimal,"and is pretty", secondadj, "and they traveled for", hours, "hours. The trip took even longer than it should have because they got stuck in a", stuckin, "for an extra", hourstwo, "hours. However, the", animal, "and the", secondanimal, "made it to", place, "all in one piece and lived happily ever after. The end.")



#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
