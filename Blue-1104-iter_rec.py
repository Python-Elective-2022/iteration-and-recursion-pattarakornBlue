def iterative_power(base, exp):
   '''
   base: int or float.
   exp: int >= 0
   returns: int or float, base^exp
   '''
   ans = base
   for times in range (1, exp):
      ans *= base
   return ans
      

print (iterative_power (5, 3))


def recursive_power(base, exp):

  '''
 
  base: int or float.

  exp: int >= 0

  returns: int or float, base^exp

  '''
  if exp == 0:
   return 1
  else:
   return (base * recursive_power(base, exp - 1)) 

print (recursive_power(10, 10))
