




#us-001/create_register

user = []


def user_register():
    id = int(input("Ingrese su id"))
    user.append(id)
    name = input("Ingrese su nombre")
    user.append(name)
    last_name = input("Ingrese su apellido")
    user.append(last_name)
    email = input("Ingrese su email")
    user.append(email)
    password = input("Cree su contraseña de 8 caracteres entre numeros y letras")
    user.append(password)
    print(user)


def user_login():
    print("Login")