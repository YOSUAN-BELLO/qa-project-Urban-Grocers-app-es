import random

# Diccionario con los datos de un nuevo usuario
user_body = {
    "firstName": "Josh",
    "phone": "+79991112233",
    "address": "Calle QA 123"
}


# Función para generar el body de un kit con un nombre específico
def get_kit_body(name):
    return {
        "name": name
    }
