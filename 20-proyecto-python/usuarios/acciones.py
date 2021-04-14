import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nOk, vamos a registrarte en el sistema...") 

        nombre = input("¿Cuál es tu nombre man? ")
        apellidos = input("¿Cuáles son tus apellidos? ")
        email = input("Introduce tu email ")
        password = input("Elige una contraseña ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")

    def login(self):
        print("\nOk, identificate en el sistema...")
        
        try:

            email = input("Introduce tu email por favor ")
            password = input("Elige una contraseña ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identifir()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto. Intentalo mas tarde.")
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        -Crear nota (crear)
        -Mostrar tus notas (mostrar)
        -Eliminar notas (eliminar)
        -Salir (salir)
        """)

        accion = input("¿Qué quiéres hacer? ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Hasta pronto {usuario[1]}")
            exit()

        return None
