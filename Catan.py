import random
AssembledTials = []
i=0
p = 17
def findprobabitly(z):
      if z == 0:
            return 0
      elif z == 2:
            return 1
      elif z == 3:
            return 2
      elif z == 4:
            return 3
      elif z == 5:
            return 4
      elif z == 6:
            return 5
      elif z == 8:
            return 5
      elif z == 9:
            return 4
      elif z == 10:
            return 3
      elif z == 11:
            return 2
      elif z == 12:
            return 1
suiteR =    ["wood","wood","wood","wood","wheat","wheat", "wheat","wheat","stone","stone"
"stone","sheep","brick","brick","brick","sheep","sheep","sheep","sheep"]
#there prob is a more efficient way to write this but all cards have both a resourse and a
##number, some of the numbers repeat
suiteNumbers = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
class Tial:
      def __init__(self, number, suite, prob):
            self.number = number
            self.suite = suite
            self.prob = prob
      #card class has 2 atributes, number and suite - this is the game Catan
Tial1 = Tial("sand",0,0)
AssembledTials.append((Tial1.number,Tial1.suite, Tial1.prob))
while len(suiteNumbers) > 0:
      q = random.randint(0,p)
      x = random.randint(0,p)
      Tial1 = Tial(suiteR[q],suiteNumbers[x],findprobabitly(suiteNumbers[x]))
      p = p-1
      #random randint is an imported function that chooses a random int in that range
      # del suiteList[Tial1.suite]
      # del suiteNumbers[Tial1.number]
      ##what I commented out is another way to do the same funtion
      
      #after the card is creating using one of the randomly genorated numbers and suites it is then deleted
      #so it is not used again
      # print(Tial1.number)
      # print(Tial1.suite)
      # print(Tial1.prob)
      
      AssembledTials.append((Tial1.number,Tial1.suite, Tial1.prob))
      rs = Tial1.suite
      rn = Tial1.number
      suiteR.remove(rn)
      suiteNumbers.remove(rs)
      i=i+1
def nextTial(i):
      return AssembledTials[i]
      i = i + 1

print("-------------/---------------------------------------CATAN BOARD----------------------------------------\ ")
print( "----------/----------",nextTial(9),"----""------",nextTial(1),"----""------",nextTial(2),"--------------------\ ")
print("--------/------/-------------------------------------\/---------------------------\------------------------------\   ")
print( "-----/-----",nextTial(3),"----""--------",nextTial(4),"----""------",nextTial(5),"----",nextTial(6),"-------------\ ")
print("----/------------/---------------------------------|---------------------------\------------------\------------------\ ")
print("---|---",nextTial(7),"----""------",nextTial(8),"----""------",nextTial(0),"----",nextTial(10),"----",nextTial(11),"---|")
print("-----\-------------\----------------------\------------------------/-------------------/----------------------------/ ")
print("--------\----",nextTial(12),"----""-------------",nextTial(13),"----""------",nextTial(14),"----",nextTial(15),"--/")
print("----------\--------\-----------------\-------------------|-------------/-------------/ --------------------------/")
print("------------\------------",nextTial(16),"----""------",nextTial(17),"----""------",nextTial(18),"--------------/")
print("---------------\---------------------------------------------------------------------------------------------/")
      ## I understand what a tuple is but why does this not want to be removed from the list
      ##It is a single variable
      ##suiteNumbers(1),suiteList(1)
      ## the goal is to get the list to print out all the terms with no repeats
      ##thank you for all your help!!!!