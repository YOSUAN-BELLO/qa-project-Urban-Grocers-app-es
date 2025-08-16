import sender_stand_request
import data

# Función de verificación positiva (respuesta 201)
def positive_assert(kit_body):
    # Obtener token de un nuevo usuario
    auth_token = sender_stand_request.get_new_user_token()
    # Crear un kit
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Verificar que el código de estado sea 201
    assert response.status_code == 201
    # Verificar que el campo name de la respuesta sea igual al enviado
    assert response.json()["name"] == kit_body["name"]

# Función de verificación negativa (respuesta 400)
def negative_assert_code_400(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400


# ===============================
# PRUEBAS DEL CHECKLIST
# ===============================

# Prueba 1. El número permitido de caracteres (1)
def test_create_kit_1_letter_name_get_success_response():
    kit_body = data.get_kit_body("a")
    positive_assert(kit_body)

# Prueba 2. El número permitido de caracteres (511)
def test_create_kit_511_letter_name_get_success_response():
    kit_body = data.get_kit_body("Abcd" * 127 + "A")  # genera 511 caracteres
    positive_assert(kit_body)

# Prueba 3. El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_letter_name_get_error_response():
    kit_body = data.get_kit_body("")
    negative_assert_code_400(kit_body)

# Prueba 4. El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letter_name_get_error_response():
    kit_body = data.get_kit_body("Abcd" * 128)  # genera 512 caracteres
    negative_assert_code_400(kit_body)

# Prueba 5. Se permiten caracteres especiales
def test_create_kit_has_special_symbol_get_success_response():
    kit_body = data.get_kit_body("\"№%@\",")
    positive_assert(kit_body)

# Prueba 6. Se permiten espacios
def test_create_kit_has_space_in_name_get_success_response():
    kit_body = data.get_kit_body(" A Aaa ")
    positive_assert(kit_body)

# Prueba 7. Se permiten números
def test_create_kit_has_number_in_name_get_success_response():
    kit_body = data.get_kit_body("123")
    positive_assert(kit_body)

# Prueba 8. El parámetro no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    kit_body = data.get_kit_body("Temporal")  # generar un body válido
    kit_body.pop("name")  # eliminar el campo "name"
    negative_assert_code_400(kit_body)

# Prueba 9. Se pasa un tipo de parámetro diferente (número en vez de string)
def test_create_kit_number_type_name_get_error_response():
    kit_body = data.get_kit_body(123)  # int en lugar de string
    negative_assert_code_400(kit_body)
