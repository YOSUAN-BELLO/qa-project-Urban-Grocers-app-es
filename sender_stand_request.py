import configuration
import requests
import data


# 🔹 Crear un nuevo usuario y devolver el authToken
def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers={"Content-Type": "application/json"}
    )


def get_new_user_token():
    response = post_new_user(data.user_body)
    print("🔹 Respuesta crear usuario:", response.status_code, response.text)  # 👈 Debug
    try:
        return response.json()["authToken"]
    except Exception as e:
        raise Exception(f"❌ No se pudo obtener authToken. Respuesta: {response.text}") from e



# 🔹 Crear un nuevo kit para un usuario específico
def post_new_client_kit(kit_body, auth_token):
    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + auth_token
        }
    )