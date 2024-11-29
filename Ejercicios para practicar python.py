"""
#1 Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print('¡Hola, mundo!')

#2 Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

mensaje = '¡Hola, mundo!'
print(mensaje)

#3 Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

nombre = input('Por favor ingrese su nombre:')
print(f'¡Hola, {nombre}!')

#4 Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 

print('El resultado de la operación es:', (((3 + 2) / (2 * 5))** 2))

#5 Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas = int(input('Por favor ingrese el número de horas trabajadas:'))
costo_hora = int(input('Ingrese el costo por horas:'))
print('El pago que le corresponde es:', (horas_trabajadas * costo_hora))

#6 Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
invertir = int((input('Ingrese la cantidad que desea invertir:')))
interes = float(input('Ingrese la tasa de interes anual:'))
años = int(input('Ingrese la cantidad de años a la que desea invertir:'))
capital = invertir * (1 + (interes / 100) ** años)
print('El capital obtenido en la inversión es:', capital)

#7 Escribir un programa que muestre por pantalla el siguiente mensaje:

print('La felicidad se puede encontrar hasta en los más oscuros')
print('momentos, si somos capaces de usar bien la luz.')
print('— Albus Dumbledore')

#8 Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
mensaje = '¡Hola Mundo!'
print(mensaje)

#9 Escribir un programa que pregunte el nombre y apellido del usuario. Luego de ser introducidos los datos muestre por pantalla la cadena ¡Hola {nombre} {apellido}, gusto en conocerte!
nombre = input('Introduce tu nombre:')
apellido = input('Introduce tu apellido:')
print(f'¡Hola {nombre} {apellido}, gusto en conocerte!')

#10 Escribir un programa que lea un entero positivo, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1. La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
n = int(input('Por favor, introduce un número positivo:'))
suma = n * (n + 1) / 2
print(f'La suma desde 1 hasta {n} es igual a {suma}')

#11 Programa que solicite al usuario los datos para calcular el área de un Cuadrado, finalmente mostrar el resultado en pantalla.
lado = int(input('Ingrese el lado de un cuadrado:'))
area = lado ** 2
print(f'El area de un cuadrado que su valor del lado es {lado} da como resultado {area} de area')

#12 Programa que solicite al usuario los datos para calcular el área de un Triángulo, finalmente mostrar el resultado en pantalla.
base = int(input('Ingrese la base de un triangulo:'))
altura = int(input('Ingrese la altura del triangulo:'))
area = (base* altura)/2
print(f'El area del triangulo que tiene como base {base} y  como altura {altura} es {area}')

#13 Programa que solicite al usuario los datos para calcular el área de un Círculo (●), finalmente mostrar el resultado en pantalla.
radio = int(input('Ingrese el area de un circulo:'))
PI = 3.1416
area = PI * (radio ** 2)
print(f'El area de un circulo que tiene como radio {radio} es igual a {area}')

#14 Programa que solicite al usuario los datos para llevar Grados Farenheit a Grados Celcius.
fahrenheit = int(input('Ingrese el valor de fahrenheit que desea pasar a grados celcius:'))
celcius = (fahrenheit - 32.0) * 5.0 / 9.0
print(f'El fahrenheit con valor {fahrenheit} convertido en grados celcius es igual a {celcius}°C.')

#15 Calculadora freelancer
dolares_hora = float(input('Ingrese la cantidad de dolares que gana por hora: '))
pago_semanal = dolares_hora * 40
pago_mensual = dolares_hora * 160
print('El valor que debe cobrar por semana trabajada es: ', pago_semanal)
print('El valor que debe cobrar al mes es: ', pago_mensual)

#16 Escribir un programa que solicite al usuario un número entero y muestre en pantalla si el número es Positivo (+) o Negativo (-). En caso de que el número sea igual a cero (0) se debe mostrar en pantalla: El número no es Positivo ni Negativo.
numero = int(input('Ingrese un número entero:'))

if numero > 0:
    print(f'El número {numero} es un positivo')
elif numero < 0:
    print(f'El número {numero} es un número negativo')
elif numero == 0:
    print('El número no es Positivo ni Negativo.')

#17 Escribir un Programa que solicite al usuario la edad de 2 personas, y diga cuál es mayor.
persona1 = input('Ingrese el nombre de la primera persona:')
persona2 = input('Ingrese el nombre de la segunda persona:')
edad1 = int(input(f'Ingrese la edad de {persona1}:'))
edad2 = int(input(f'Ingrese la edad de {persona2}:'))

if edad1 > edad2:
    print(f'{persona1} es mayor que {persona2}')
elif edad1 < edad2:
    print(f'{persona2} es mayor que {persona1}')
elif edad1 == edad2:
    print(f'{persona1} y {persona2} tienen la misma edad')

#18 Introducir un número por teclado y que se muestre un mensaje indicando si es par o impar.
numero = int(input('Ingrese un número:'))
if numero % 2 == 0:
    print(f'El número {numero} es par.')
else:
    print(f'El número {numero} es impar')

#19 Introducir un número por teclado y que se muestre un mensaje indicando si es múltiplo de 3.
numero = int(input('Ingrese un número:'))
if numero % 3 == 0:
    print(f'El número {numero} es multiplo de 3.')
else:
    print(f'El número {numero} no es multiplo de 3')

#20 Escribir un programa que solicite al usuario una letra y diga si esta es MAYÚSCULA o minúscula.
letra = input('Ingrese una letra:')
if letra <= 'z' and letra >= 'a':
    print(f'La letra "{letra}" es minuscula')
elif letra <= 'Z' and letra >= 'A':
    print(f'La letra {letra} es MAYUSCULA')
else:
    print(f'Error: El caracter ingresado no es una letra')
 
#21 Escribir un programa que solicite al usuario 3 números, compararlos y decir cual es mayor.
num1 = int(input('Ingrese el primer número:'))
num2 = int(input('Ingrese un segundo número:'))
num3 = int(input('Ingrese un tercer número:'))
numeros = [num1, num2, num3]

if num1 > num2:
    if num1 > num3:
        maximo = num1
    else:
        maximo = num3
else:
    if num2 > num3:
        maximo = num2
    else:
        maximo = num3

print('El número mayor de la lista es:', maximo)
  
#22 Escribir un programa que solicite al usuario 5 números, compararlos y decir cual es mayor.
num1 = int(input('Ingrese el primer número:'))
num2 = int(input('Ingrese el segundo número:'))
num3 = int(input('Ingrese el tercer número:'))
num4 = int(input('Ingrese el cuarto número:'))
num5 = int(input('Ingrese el quinto número:'))
numeros = [num1, num2, num3, num4, num5]

def listanumeros(lista):
    maximo = max(lista)
    return maximo

valor = listanumeros(numeros)
print('El valor maximo almacenado en la lista es:', valor)

#23 Escribir un programa en el cual se solicite al usuario un número y se imprima la tabla de multiplicar del 1 al 10 del valor introducido.
multiplicador = 1
resultado = 0
numero = 0
 
numero = int(input('>>> Introduce el numero a multiplicar: '))
 
while multiplicador > 0 and multiplicador < 11:
    resultado = numero * multiplicador
    print("%d x %2d = %d" %(numero,multiplicador,resultado))
    multiplicador = multiplicador + 1

numero = int(input('>>> Introduce el numero a multiplicar: '))
 
for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print("%d x %2d = %d" % (numero,multiplicador,resultado))

#24 Escribir un programa que imprima los números pares entre 0 y 200 de forma creciente.
print('Imprimir los numeros pares entre 0 y 200 de forma Creciente')
 
for pares in range(0, 201):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)

#25 Escribir un programa que imprima los números pares entre el 0 y 200 de forma decreciente.
print('Números pares de manera descreciente:')

for pares in range(201, -1, -1):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)

#26 Escribir un programa que imprima los números pares de forma creciente hasta un número introducido por el usuario.
numero = int(input('Ingrese el número limite del conteo:'))
for pares in range(0, numero):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)

#27 Escribir un programa que imprima todos los números primos hasta un número introducido por el usuario.
numero = int(input('Introduzca un número:'))
def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(f'Los números primos hasta {numero} son: ')
for num in range(2, numero + 1):
    if es_primo(num):
        print(num)
""" 
print('Sistema de Reserva de Hoteles')

clientes = 'Laura'
dias = 5
tarifa_diaria = 1200.00
habitacion = True

print('Cliente:', clientes)
print('Días de estancia:', dias)
print('Tarifa diaria:', tarifa_diaria)
print('¿Habitación con vista al mar?:', habitacion)

