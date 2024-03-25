import hashlib

def comprovarCrednecials(crendenciales):
    lista = []
    flag = 0
    try:
        with open("Usuaris.txt","r") as file:
            lectura = file.readlines()

        for linia in lectura:
            elemento = linia.strip().replace("|", ",").split(",")
            lista.append(elemento)

        lista = lista[1:4]

        for i in lista:
            if i == crendenciales:
                flag+=1 
                 
        return flag

    except FileNotFoundError:
        print("L'arxiu no exsisteix")



def accions_a_realitzar():

    print("BIBLIOTECA CAN CASACUBERTA")
    print("=============================")
    print("1: Mostrar un libro")
    print("2: Mostrar todos los libros")
    print("3: Añadir un libro")
    print("4: Eliminar un libro")
    print("5: Editar un libro")
    print("6: Salir del programa")
    print("\n")
    try:
        accion = int(input("Ingresa la accion a realizar: "))
    except ValueError:
        print("Inserta un numero si us plau")

    if accion == 6:
        return
    
   
def encriptar(passwd):
    
    contraseña_cifrada = hashlib.md5(passwd.encode('utf-8'))
    hash_hexadecimal = contraseña_cifrada.hexdigest()
    return hash_hexadecimal


def inicioSesion():
    intento = 3

    print("********************")
    print("***INICIAR SESION***")
    print("********************")

    while True:

        print("Queda", intento, "intentos")

        usuari = input("Ingresa el nombre de usuario: ")
        contraseña = input("Ingresa la contraseña: ")
        print("\n")

        contraseña_cifrada = encriptar(contraseña)

        crendenciales = [usuari, contraseña_cifrada]
        resultado = comprovarCrednecials(crendenciales)

        if intento == 1:
            print("Saliendo del programa...")
            break

        if resultado > 0:
            accions_a_realitzar()
            break
        else:
            intento -=1

 
inicioSesion()