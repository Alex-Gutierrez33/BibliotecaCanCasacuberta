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
    if accion == 4:
        eliminarLlibre()
    if accion == 5:
        editarLibro()
    

def editarLibro():

    lista = []
    listaDiccionario = []
    listaFinal = []
    listaCamps = []
    error = 0

    try:
        with open("Llibres.txt","r") as OpenFile:
            lectura = OpenFile.readlines()

            for libro in lectura:
                elemento = libro.strip().replace("|", ",").split(",")
                lista.append(elemento)

    except FileNotFoundError:
        print("No se ha encontrado el archivo")


    for i in lista:
        titol, autor, any, genere, isbn = i
        dic = {"titol": titol, "autor":autor, "any": any, "genere": genere, "isbn": isbn}
        listaDiccionario.append(dic)


    obraModificar = input("Ingresa el nombre de la obra a modificar: ")

    contador = 0
    for libro in listaDiccionario:
        obra = libro["titol"]
        if obra == obraModificar:
            contador +=1
        
    if contador == 1:
        campoModificar = input("Ingresa un campo a modificar: ")
        if campoModificar == "titol" or campoModificar == "autor" or campoModificar == "any" or campoModificar == "genere" or campoModificar == "isbn":

            valor = input("Ingresa el valor: ")

            for libro in listaDiccionario:
                if libro["titol"] == obraModificar:
                    libro[campoModificar] = valor
                listaFinal.append(libro)

        else:
            print("Este campo no exisite")

            with open("Llibres.txt", "w") as file:   
                for libro in listaDiccionario:
                    valores = list(libro.values())
                    listaCamps.append(valores)
                
                for i in listaCamps:
                    obra = i[0] + "|" + i[1] + "|" + i[2] + "|" + i[3] + "|" + i[4] + "\n"
                    file.writelines(obra)
            error = 1
    else:
        print("La obra solicitada no esta disponible acutalmente")

        with open("Llibres.txt", "w") as file:   
            for libro in listaDiccionario:
                valores = list(libro.values())
                listaCamps.append(valores)
                
            for i in listaCamps:
                obra = i[0] + "|" + i[1] + "|" + i[2] + "|" + i[3] + "|" + i[4] + "\n"
                file.writelines(obra)

    for libro in listaFinal:
        valores = list(libro.values())
        listaCamps.append(valores)

    print("\n")

    if contador == 1 and error != 1:

        print("RESULTADO OBRAS")
        print("***************")

        id = 1

        for i in listaCamps:
            libro = " ".join(i)
            cadena = str(id) + "." + libro
            id+=1
            print(cadena)

    try:
        with open("Llibres.txt", "w") as file:
            for i in listaCamps:
                obra = i[0] + "|" + i[1] + "|" + i[2] + "|" + i[3] + "|" + i[4] + "\n"
                file.writelines(obra)

    except FileNotFoundError:
        print("El archivo no se ha encontrado")

def eliminarLlibre():

    lista = []
    listaNueva = []
    contador = 0

    try:
        with open("Llibres.txt", "r") as OpenFile:
            lectura = OpenFile.readlines()
    except FileNotFoundError:
        print("No s'ha trobat el arxiu")

    else:

        for libro in lectura:
            elemento = libro.strip().replace("|", ",").split(",")
            lista.append(elemento)

        llibreEliminar = input("Indica el nom del llibre a eliminar: ")


        for libro in lista:
            titol, autor, any, genere, isbn = libro

            
            if titol != llibreEliminar:
                listaNueva.append(libro)
                contador +=1

        if contador == len(lista):
            print("ERROR: No se ha encontrado el libro")

            with open("Llibres.txt", "w") as file:
                for i in listaNueva:
                    titol, autor, any, genere, isbn = i
                    linia = titol + "|" + autor + "|" + any + "|" + genere + "|" + isbn + "\n"
                    file.writelines(linia)

        print("LLibres restants: ")
        print("===================")
        print("\n")

        listaMostrar = listaNueva[1:]
        id = 1

        for i in listaMostrar:
            titol, autor, any, genere, isbn = i
            print(id, titol)
            id+=1

        
        with open("Llibres.txt", "w") as file:
            for i in listaNueva:
                titol, autor, any, genere, isbn = i
                linia = titol + "|" + autor + "|" + any + "|" + genere + "|" + isbn + "\n"
                file.writelines(linia)

        

def encriptar(passwd):
    
    contraseña_cifrada = hashlib.md5(passwd.encode('utf-8'))
    hash_hexadecimal = contraseña_cifrada.hexdigest()
    return hash_hexadecimal


def inicioSesion():
    intento = 3

    print("********************")
    print("***INICIAR SESION***")
    print("********************")

    while intento > 0:

        print("Queda", intento, "intentos")


        usuari = input("Ingresa el nombre de usuario: ")
        contraseña = input("Ingresa la contraseña: ")
        print("\n")

        contraseña_cifrada = encriptar(contraseña)

        crendenciales = [usuari, contraseña_cifrada]
        resultado = comprovarCrednecials(crendenciales)

        if resultado > 0:
            accions_a_realitzar()
            break

        intento -= 1 

        if intento == 0:
            print("Saliendo del programa...")

        

 
inicioSesion()