import math
print('**Welcome to My Calculator**\n')
def intro():
    print('1)To find Square Root of Number.')
    print('2)To find Square of Number.')
    print('3)To find Cube of Number.')
    print('4)To Check Number prime or not')
    print('5)To find Factorial of Number.')
    print('6)To find Prime Factors of Number.')
    print('0)To Exit the Program.\n')
    
    value=int(input('Enter The Input:'))
    
    if (value==1):
        calculate.sqroot()
    elif (value==2):
        calculate.square()
    elif (value==3):
        calculate.cube()
    elif (value==4):
        calculate.is_prime()
    elif (value==5):
        calculate.factorial_inbuild()
    elif (value==6):
        calculate.factors()
    elif (value==0):
        outro()
    else:
        print('Invalid Input.')

def outro():
        print('** THANK YOU **')
        
class calculate:

  def sqroot():
    X=int(input('\nTo Find Square Root of Number.\nEnter The Number:'))
    print("The Square Root of", X, "is", math.sqrt(X))

  def square():
    Y=int(input('\nTo Find Square of Number.\nEnter The Number:'))
    print("The Square of", Y, "is", Y**2)

  def cube():
    Z=int(input('\nTo Find Cube of Number.\nEnter The Number:'))
    print("The Cube of", Z, "is", Z**3)

  def is_prime():
    XX=int(input('\nTo Check Prime or Not.\nEnter The Number:'))
    if XX < 2:
      print(XX, "is not a Prime Number")
    else:
      for i in range(2, XX):
        if XX % i == 0:
          print(XX, "is not a Prime Number")
          break
      else:
        print(XX, "is a Prime Number")

  def factorial_inbuild():
    YY=int(input('\nTo Find Factorial of Number.\nEnter The Number:'))
    print("Factorial of", YY, "is", math.factorial(YY))

  def factors():
    def prime_factors(YZ):
        prime_factors_list = []
        i = 2

        while i <= YZ:
            if YZ % i == 0:
                prime_factors_list.append(i)
                YZ = YZ // i
            else:
                i += 1

        return prime_factors_list

    number = int(input('\nTo Find Prime Factors of Number.\nEnter The Number:'))
    prime_factors_list = prime_factors(number)
    print("Prime Factors:", prime_factors_list)

intro()