# int
number = 10
result = number + 10

result_multiplication = number * 10
result_division = number / 2 # debido al simbolo "/" siempre se va a obtener como resultado un número flotante

# NOTA: si queremos obtener un numero entero como resultado, debemos usar "//" (doble barra)
result_division_int = number // 2




print("the result is:", result)
print("The multiplication's result is:", result_multiplication)
print("The division's result is:", result_division)
print("The integer division's result is:", result_division_int)

# se puede usar "_" para que los números grandes sean legibles para el ojo humano
# ejemplo: 10_000_000_000 es lo mismo que 10000000000

big_number = 10_000_000_000

print("big number: ", big_number)