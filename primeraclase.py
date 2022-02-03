miNombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
print("Hola de nuevo " + miNombre + ". Tu edad es: " + edad)

comida = input("Comida favorita: ")


if comida == "pizza" :
    tipoPizza = input("Cuál es tu pizza favorita: ")
    if tipoPizza == "pepperoni" :
        print("Me gusta la pizza de  pepperoni")
    else:
        print("Me gusta todo tipo de pizza")
else:
    print("No me gusta la pizza")
