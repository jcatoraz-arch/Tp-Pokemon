import json
import os
import random
from pokemon import Pokemon
from estructuras.hash_map import HashMap
from estructuras.hash_set import HashSet
from estructuras.lista_enlazada import ListaEnlazada
from estructuras.queue import Queue
from algoritmos.ordenamientos import *
from estructuras.stack import Stack

def limpiar_pantalla():
    os.system("cls")

def cargar_pokedex():
    pokedex = HashMap()
    with open("data/pokedex.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        for p in datos:
            pokemon = Pokemon(p["id"], p["nombre"], p["tipo"], p["poder_combate"])
            pokedex.insertar(pokemon.id, pokemon)
    return pokedex

def cargar_medallas():
    medallas = HashSet()
    with open("data/medallas.txt", "r", encoding="utf-8") as archivo:
        lineas = [linea.strip() for linea in archivo]
    medallas.agregar(lineas[0])
    medallas.agregar(lineas[1])
    return medallas

def cargar_gimnasios():
    with open("data/medallas.txt", "r", encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo]
    
def mostrar_equipo(equipo):
    if len(equipo) == 0:
        print("No hay Pokemon en el equipo aun")
    else:
        for pokemon in equipo:
            print(pokemon)

def buscar_pokemon(nombre, lista):
    for pokemon in lista:
        if pokemon.nombre.lower() == nombre.lower():
            return pokemon
    return None

def mostrar_menu():
    print("POKEMON HUERGO:")
    print("1. Ver Pokedex")
    print("2. Ver Equipo Principal")
    print("3. Ver PC")
    print("4. Capturar Pokemon")
    print("5. Ordenar PC")
    print("6. Buscar Pokemon en Equipo")
    print("7. Enviar Pokemon al Centro Pokemon")
    print("8. Transferir Pokemon al Profesor Oak")
    print("9. Deshacer ultima transferencia")
    print("10. Desafiar Lider de Gimnasio")
    print("11. Ver medallas")
    print("0. Salir")

pokedex = cargar_pokedex()
medallas = cargar_medallas()
print(medallas.valores())
gimnasios = cargar_gimnasios()
transferencias = Stack()

equipo_principal = []
print("Cantidad de Pokemon cargados:", len(list(pokedex.valores())))
pc = ListaEnlazada()
centro_pokemon = Queue()

while True:
    limpiar_pantalla()
    mostrar_menu()

    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        print("POKEDEX:")
        for pokemon in pokedex.valores():
            print(pokemon)
        input("Presione enter para continuar")

    elif opcion == "2":
        print("EQUIPO PRINCIPAL: ")
        mostrar_equipo(equipo_principal)
        input("Presione enter para continuar")

    elif opcion == "3":
        print("PC POKEMON:")
        pc.mostrar()
        input("Presione enter para continuar")

    elif opcion == "4":
        pokemon = random.choice(list(pokedex.valores()))
        print(f"Aparecio un {pokemon.nombre}")
        if len(equipo_principal) < 6:
            equipo_principal.append(pokemon)
            print(f"{pokemon.nombre} agregado al equipo")
        else:
            pc.agregar_inicio(pokemon)
            print(f"Equipo lleno. {pokemon.nombre} enviado a la PC")
        input("Presione enter para continuar")

    elif opcion == "5":
        print("ORDENAR PC:")
        print("1 - Ordenar por nombre")
        print("2 - Ordenar por tipo")
        print("3 - Ordenar por poder de combate")
        opcion_orden = input("Seleccione una opcion: ")
        lista_pc = pc.a_lista()
        if opcion_orden == "1":
            bubble_sort_nombre(lista_pc)
            pc.desde_lista(lista_pc)
            print("PC ordenada por nombre")
        elif opcion_orden == "2":
            insertion_sort_tipo(lista_pc)
            pc.desde_lista(lista_pc)
            print("PC ordenada por tipo")
        elif opcion_orden == "3":
            lista_pc = quick_sort_poder(lista_pc)
            pc.desde_lista(lista_pc)
            print("PC ordenada por poder de combate")
        else:
            print("Opcion invalida")
        input("Presione enter para continuar")

    elif opcion == "6":
        nombre = input("Ingrese el nombre del Pokemon: ")
        pokemon = buscar_pokemon(nombre, equipo_principal)
        if pokemon:
            print("Pokemon encontrado:")
            print(pokemon)
        else:
            print("Pokemon no encontrado")
        input("Presione enter para continuar")

    elif opcion == "7":
        if len(equipo_principal) == 0:
            print("No hay Pokemon en el equipo")
        else:
            for pokemon in equipo_principal:
                centro_pokemon.encolar(pokemon)
            print("Curando equipo, espere unos segundos")
            while not centro_pokemon.esta_vacia():
                pokemon = centro_pokemon.desencolar()
                print(f"{pokemon.nombre} ha sido curado")
        input("Presione enter para continuar")

    elif opcion == "8":
        print("POKEMON EN LA PC:")
        pc.mostrar()
        id_pokemon = int(input("Ingrese el ID del pookemon a transferir: "))
        pokemon = pc.transferir_por_id(id_pokemon)
        if pokemon:
            transferencias.apilar(pokemon)
            print(f"{pokemon.nombre} fue transferido al profesor Oak")
        else:
            print("No existe un pokemon con ese ID en la PC")
        input("Presione enter para continuar")

    elif opcion == "9":
        pokemon = transferencias.desapilar()
        if pokemon:
            pc.agregar_inicio(pokemon)
            print(f"{pokemon.nombre} volvio a la PC")
        else:
            print("No hay transferencias para deshacer")
        input("Presione enter para continuar")

    elif opcion == "10":
        if len(equipo_principal) == 0:
            print("Tu equipo esta vacio, primero captura pokemones")
            input("Presione enter para continuar")
        else:
            print("GIMNASIOS:")
            for i in range(len(gimnasios)):
                print(f"{i + 1}. {gimnasios[i]}")
            opcion_gimnasio = int(input("Seleccione un gimnasio: "))
            if 1 <= opcion_gimnasio <= len(gimnasios):
                medalla = gimnasios[opcion_gimnasio - 1]
                gano = random.choice([True, False])
                if gano:
                    print("¡¡Ganaste la batalla!!")
                    if medallas.contiene(medalla):
                        print("Ya tenias esta medalla")
                    else:
                        medallas.agregar(medalla)
                        print(f"Obtuviste la {medalla}")
                else:
                    print("Perdiste la batalla")
            else:
                print("Gimnasio invalido")
            input("Presione enter para continuar")

    elif opcion == "11":
        print("MEDALLAS:")
        for medalla in medallas.valores():
            print(medalla)        
        input("Presione enter para continuar")

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opcion invalida")