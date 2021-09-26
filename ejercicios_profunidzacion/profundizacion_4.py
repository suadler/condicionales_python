# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

word_1 = str(input("insert first word"))
word_2 = str(input("insert second word"))
word_3 = str(input("insert third word"))

length_word_1 = len(word_1)
lenght_word_2 = len(word_2)
lenght_word_3 = len(word_3)

order = int(input("insert 1 if your would like to order alphabetically or 2 if you would like to oder by number of letters: "))

if (order == 1):
    if (word_1 >= word_2) and (word_1 >= word_3) and (word_2 >= word_3):
        print("order: ", word_1, word_2, word_3)
    elif (word_1 >= word_2) and (word_1 >= word_3) and (word_3 >= word_2):
        print("order: ", word_1, word_3, word_2)
    elif (word_2 >= word_1) and (word_2 >= word_3) and (word_1 >= word_3):
        print("order: ", word_2, word_1, word_3)
    elif (word_2 >= word_1) and (word_2 >= word_3) and (word_3 >= word_1):
        print("order: ", word_2, word_3, word_1)
    elif (word_3 >= word_1) and (word_3 >= word_2) and (word_1 >= word_2):
        print("order: ", word_3, word_1, word_2)
    elif (word_3 >= word_1) and (word_3 >= word_2) and (word_2 >= word_1):
        print("order: ", word_3, word_2, word_1)

elif (order == 2):
    if (length_word_1 >= lenght_word_2) and (length_word_1 >= lenght_word_3) and (lenght_word_2 >= lenght_word_3):
        print("order: ", length_word_1, lenght_word_2, lenght_word_3)
    elif (length_word_1 >= lenght_word_2) and (length_word_1 >= lenght_word_3) and (lenght_word_3 >= lenght_word_2):
        print("order: ", length_word_1, lenght_word_3, lenght_word_2)
    elif (lenght_word_2 >= length_word_1) and (lenght_word_2 >= lenght_word_3) and (length_word_1 >= lenght_word_3):
        print("order: ", lenght_word_2, length_word_1, lenght_word_3)
    elif (lenght_word_2 >= length_word_1) and (lenght_word_2 >= lenght_word_3) and (lenght_word_3 >= length_word_1):
        print("order: ", lenght_word_2, lenght_word_3, length_word_1)
    elif (lenght_word_3 >= length_word_1) and (lenght_word_3 >= lenght_word_2) and (length_word_1 >= lenght_word_2):
        print("order: ", lenght_word_3, length_word_1, lenght_word_2)
    elif (lenght_word_3 >= length_word_1) and (lenght_word_3 >= lenght_word_2) and (lenght_word_2 >= length_word_1):
        print("order: ", lenght_word_3, lenght_word_2, length_word_1)

    
