# Entero: int numero = 5

# Flotante: float precio = 10.5

# Caracter: char letra = 'A'

# Booleano: boolean esVerdadero = true


nombre = "Juan"
edad = 30
altura = 1.75

resultado = nombre + " tiene " + \
    str(edad) + " años y mide " + str(altura) + " metros."
print(resultado)


# En Python, el límite de los enteros está determinado por la arquitectura de la plataforma en la que se ejecuta el código. En sistemas de 32 bits, el límite de los enteros es de -2,147,483,648 a 2,147,483,647. Mientras que en sistemas de 64 bits, el rango de los enteros es mucho mayor, de -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807.

# Por otro lado, los números de punto flotante en Python siguen el estándar de precisión doble de IEEE 754, lo que significa que tienen una precisión de 64 bits. El rango de los números flotantes en Python va desde alrededor de 2.3e-308 a 1.7e+308, y la precisión es de aproximadamente 15-16 dígitos decimales.

# Es importante tener en cuenta que debido a la representación binaria de los números de punto flotante, pueden ocurrir errores de redondeo al realizar operaciones aritméticas con ellos. Es recomendable tener precaución al trabajar con números de punto flotante en Python para evitar estos errores.

n = 5  # Cantidad de números pares a sumar

suma = n * (n + 1)

print("La suma de los primeros", n, "números pares es:", suma)
