import json
from pokemon import Pokemon
from estructuras.hash_map import HashMap

def cargar_pokedex():
    pokedex = HashMap()
    with open("data/pokedex.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        for p in datos:
            pokemon = Pokemon(p["id"], p["nombre"], p["tipo"], p["poder_combate"])
            pokedex.insertar(pokemon.id, pokemon)
    return pokedex

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
equipo_principal = []
print("Cantidad de Pokemon cargados:", len(list(pokedex.valores())))

while True:
    mostrar_menu()

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print("=== POKEDEX ===")

        for pokemon in pokedex.valores():
            print(pokemon)

    elif opcion == "2":
        print("Ver Equipo Principal")

    elif opcion == "3":
        print("Ver PC")

    elif opcion == "4":
        print("Capturar Pokemon")

    elif opcion == "5":
        print("Ordenar PC")

    elif opcion == "6":
        print("Buscar Pokemon en Equipo")

    elif opcion == "7":
        print("Enviar Pokemon al Centro Pokemon")

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