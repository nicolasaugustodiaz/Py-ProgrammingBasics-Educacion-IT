def solicitar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            pass


a = solicitar_numero("Escribe un número: ")
b = solicitar_numero("Escribe otro número: ")

print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
try:
    print("a / b:", a / b)
except ZeroDivisionError:
    print("No se puede dividir por cero.")