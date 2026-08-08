"""
OPERADORES RELACIONALES
--------------------------
== : igual
> : mayor
>= : mayor o igual
< : menor
<= : menor o igual
!= : distinto

OPERADORES LOGICOS
-------------------
and
or
not



nos permite comparar dos valores



"""

number_one = 10
number_two = 20
result_one = number_one == number_two
print("The result of comparison is:", result_one)
print(type(result_one))


logic_value_one = True
logic_value_two = True

result_logic_operators = logic_value_one and logic_value_two # True

print("the logic operator result is:", result_logic_operators)


complex_result = (
  (number_one == number_two and True)
  and (number_one < 100)
  and (number_two < 100)
  or (number_one > 100 and number_two > 200)
  )

print(not complex_result)