import random
i=0
suiteR =    ("wood","wood","wood","wood","wheat","wheat", "wheat","wheat","stone","stone"
"stone","sheep","brick","brick","brick","sheep","sheep","sheep","sand")
#there prob is a more efficient way to write this but all cards have both a resourse and a
##number, some of the numbers repeat
suiteNumbers = (6,5,9,4,3,8,10,6,5,9,12,3,2,10,11,11,4,8,0)
class Tial:
      def __init__(self, number, suite):
            self.number = number
            self.suite = suite
      #card class has 2 atributes, number and suite - this is the game Catan
while i < 19:
      Tial1 = Tial(suiteR[random.randint(0,18)],suiteNumbers[random.randint(0,18)])
      #random randint is an imported function that chooses a random int in that range
      # del suiteList[Tial1.suite]
      # del suiteNumbers[Tial1.number]
      ##what I commented out is another way to do the same funtion
      suiteR.remove(Tial1.suite)
      suiteNumbers.remove(Tial1.number)
      #after the card is creating using one of the randomly genorated numbers and suites it is then deleted
      #so it is not used again
      print(Tial1.number)
      print(Tial1.suite)
      i=i+1
      ## I understand what a tuple is but why does this not want to be removed from the list
      ##It is a single variable
      ##suiteNumbers(1),suiteList(1)
      ## the goal is to get the list to print out all the terms with no repeats
      ##thank you for all your help!!!!