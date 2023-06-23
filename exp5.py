import math


class calculate:

  def sqroot(X):
    print("The Square Root of", X, "is", math.sqrt(X))

  def square(Y):
    print("The Square of", Y, "is", Y**2)

  def cube(Z):
    print("The Cube of", Z, "is", Z**3)

  def is_prime(XX):
    if XX < 2:
      print(XX, "is not a Prime Number")
    else:
      for i in range(2, XX):
        if XX % i == 0:
          print(XX, "is not a Prime Number")
          break
      else:
        print(XX, "is a Prime Number")

  def factorial_inbuild(YY):
    print("Factorial of", YY, "is", math.factorial(YY))

  def factorial_ordinary(XY):
    num = 1
    factorial = 1
    while num <= XY:
      factorial = factorial * num
      num += 1
    print("Factorial of", XY, "is", factorial)

  def prime_factors(YZ):
    factors = []
    i = 2

    while i <= YZ:
        if YZ % i == 0:
            factors.append(i)
            YZ = YZ // i
        else:
            i += 1

    return factors

number = 80
factors = calculate.prime_factors(number)


calculate.sqroot(4)
calculate.square(3)
calculate.cube(5)
calculate.is_prime(9)
calculate.is_prime(7)
calculate.is_prime(-11)
calculate.factorial_inbuild(4)
calculate.factorial_ordinary(4)
print("Prime factors of", number, "are:", factors)
