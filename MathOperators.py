# Math operators

# import math 
# Math in programming is the same as real life math
# syntaxwise

my_int1 = 5
my_int2 = 3

# Operations:
# 1. Addition (+)
add_result = my_int1 + my_int2

print(str(my_int1) + " + " + str(my_int2) + " = " + str(add_result))

# 2. Substraction (-)
subs_result = my_int1 - my_int2

print(str(my_int1) + " - " + str(my_int2) + " = " + str(subs_result))

# 3. Products (*) (We use the '*' character)
prod_result = my_int1 * my_int2

print(str(my_int1) + " * " + str(my_int2) + " = " + str(prod_result))

# 4. Divisions (/) (We use the '/' character)
div1_result = my_int1 / my_int2

print(str(my_int1) + " / " + str(my_int2) + " = " + str(div1_result))

# Note: If we want a close division (as an int with no floating points we use '//')
div2_result = my_int1 // my_int2

print(str(my_int1) + " // " + str(my_int2) + " = " + str(div2_result))
# It will be rounded to the lower limit

# 5. Powers (**) (We use this as the exponential operator ('**'))
pow_result = my_int1 ** my_int2

print(str(my_int1) + " ** " + str(my_int2) + " = " + str(pow_result))

# 6. Modulus operator (%) (We use this to get the remainder
# of a division -> It is one of the most important operators
# for complex operations like prime number gathering, or 
# pseudo-random number generation)

mod_result = my_int1 % my_int2

print(str(my_int1) + " % " + str(my_int2) + " = " + str(mod_result))

# 7. Square root (math.sqrt())
# We use the sqrt() method built in the math library we imported at line 3
'''
my_int3 = 49
sqrt_result = math.sqrt(my_int3)

print("Square root of " + str(my_int3) + " = " + str(sqrt_result))
'''