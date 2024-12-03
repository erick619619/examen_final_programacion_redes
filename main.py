import requests
import json

# URL base correcta
APIHOST = "http://library.demo.local/api/v1"  # Endpoint base de la API

# Credenciales de acceso (usuario y contraseña)
LOGIN = "cisco"
PASSWORD = "Cisco123!"

# Función para obtener el token de autenticación
def getAuthToken():
    AuthCreds = (LOGIN, PASSWORD)
    try:
        # Solicitud POST para obtener el token
        r = requests.post(f"{APIHOST}/loginViaBasic", auth=AuthCreds)
        r.raise_for_status()  # Verifica si la solicitud fue exitosa
        return r.json()["token"]  # Devuelve el token si la solicitud fue exitosa
    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a la API: {e}")
        return None

# Función para agregar un libro a la biblioteca
def addBook(book, apiKey):
    try:
        # Headers necesarios para la solicitud
        headers = {
            "Content-type": "application/json",
            "X-API-key": apiKey  # Usando el token como API Key
        }
        # Realizamos la solicitud POST para agregar el libro
        r = requests.post(f"{APIHOST}/books", headers=headers, data=json.dumps(book))
        r.raise_for_status()  # Verifica si la solicitud fue exitosa
        print(f"Libro {book} agregado.")  # Imprime mensaje si el libro se agrega correctamente
    except requests.exceptions.RequestException as e:
        print(f"Error al agregar libro: {e}")  # Muestra el error si algo falla

# Obtener el token de autenticación
apiKey = getAuthToken()

if apiKey:
    # Crear un libro con los detalles proporcionados directamente en el código
    book_data = {
        "id": 20,
        "title": "examen final",
        "author": "erick amador chucusea"
    }
    
    # Agregar el libro a la API
    addBook(book_data, apiKey)
else:
    print("No se pudo obtener el token de autenticación.")
