import json
from pokemon import Pokemon
from estructuras.hash_map import HashMap
from estructuras.hash_set import HashSet
from estructuras.lista_enlazada import ListaEnlazada
from estructuras.queue import Queue

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
    with open("data/medallas.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        medallas.agregar(datos[0])
        medallas.agregar(datos[1])
    return medallas

def mostrar_equipo(equipo):
    if len(equipo) == 0:
        print("No hay Pokemon en el equipo aun")
    else:
        for pokemon in equipo:
            print(pokemon)

def mostrar_menu():
    print("=== POKEMON HUERGO ===")
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
    print("0. Salir")

pokedex = cargar_pokedex()
medallas = cargar_medallas()
print(medallas.valores())

equipo_principal = []
print("Cantidad de Pokemon cargados:", len(list(pokedex.valores())))
pc = ListaEnlazada()
centro_pokemon = Queue()

while True:
    mostrar_menu()

    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        print("=== POKEDEX ===")
        for pokemon in pokedex.valores():
            print(pokemon)

    elif opcion == "2":
        print("=== EQUIPO PRINCIPAL ===")
        mostrar_equipo(equipo_principal)

    elif opcion == "3":
        print("=== PC POKEMON ===")
        pc.mostrar()

    elif opcion == "4":
        id_pokemon = int(input("Ingrese el ID del Pokemon a capturar: "))
        pokemon = pokedex.obtener(id_pokemon)
        if pokemon:
            if len(equipo_principal) < 6:
                equipo_principal.append(pokemon)
                print(f"{pokemon.nombre} agregado al equipo")
            else:
                pc.agregar_inicio(pokemon)
                print(f"Equipo lleno, {pokemon.nombre} enviado a la PC")
        else:
            print("Pokemon no encontrado")

    elif opcion == "5":
        print("Ordenar PC")

    elif opcion == "6":
        print("Buscar Pokemon en Equipo")

    elif opcion == "7":
        if len(equipo_principal) == 0:
            print("No hay Pokemon en el equipo")
        else:
            for pokemon in equipo_principal:
                centro_pokemon.encolar(pokemon)
            print("Curando equipo...")
            while not centro_pokemon.esta_vacia():
                pokemon = centro_pokemon.desencolar()
                print(f"{pokemon.nombre} ha sido curado")

    elif opcion == "8":
        print("Transferir Pokemon al Profesor Oak")

    elif opcion == "9":
        print("Deshacer ultima transferencia")

    elif opcion == "10":
        print("Desafiar Lider de Gimnasio")

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opcion invalida")