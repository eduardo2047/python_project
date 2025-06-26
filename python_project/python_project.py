
libros = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967},
    {"titulo": "1984", "autor": "George Orwell", "año": 1949},
    {"titulo": "El nombre del viento", "autor": "Patrick Rothfuss", "año": 2007},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "año": 1605},
    {"titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "año": 1981}
]


def mostrar_libros(lista):
    for libro in lista:
        print(f"{libro['titulo']} - {libro['autor']} ({libro['año']})")
    print()


def ordenar_libros(criterio):
    if criterio in ["titulo", "autor", "año"]:
        return sorted(libros, key=lambda x: x[criterio])
    else:
        print("Criterio no válido. Usa: 'titulo', 'autor' o 'año'.")
        return libros


def menu():
    print("¿Cómo quieres ordenar la lista de libros?")
    print("1. Por título")
    print("2. Por autor")
    print("3. Por año de publicación")
    opcion = input("Elige una opción (1, 2, 3): ")

    if opcion == "1":
        ordenados = ordenar_libros("titulo")
    elif opcion == "2":
        ordenados = ordenar_libros("autor")
    elif opcion == "3":
        ordenados = ordenar_libros("año")
    else:
        print("Opción inválida.")
        return

    print("\nLista de libros ordenada:")
    mostrar_libros(ordenados)


menu()