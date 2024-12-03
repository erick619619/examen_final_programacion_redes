import json

# Abre y carga el archivo JSON
with open('usuarios.json', 'r') as file:
    usuarios = json.load(file)

# Extrae y muestra los nombres de los usuarios
for usuario in usuarios:
    print(usuario['nombre'])
