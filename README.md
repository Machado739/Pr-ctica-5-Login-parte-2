# Practica-5-Login-parte-2

Este proyecto es una aplicación web desarrollada con el framework Flask en Python. La aplicación tiene como objetivo principal gestionar el inicio de sesión de usuarios, verificando sus credenciales en una base de datos MySQL. A continuación, se proporciona una descripción detallada de diferentes aspectos del proyecto:

## Paquetes Utilizados

- **Flask**: Framework web para Python.
- **Flask-MySQLdb**: Extensión para integrar MySQL con Flask.
- **MySQL Connector**: Módulo para interactuar con bases de datos MySQL en Python.

## Configuración de la Base de Datos

Se utiliza MySQL como sistema de gestión de base de datos. En el archivo `app.py`, se configuran los detalles de la base de datos en la clase `DevelopmentConfig`, que contiene los parámetros como host, usuario, contraseña y nombre de la base de datos.

```python
class DevelopmentConfig:
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = "usuario1"
    MYSQL_PASSWORD = "Machador0231."
    MYSQL_DB = "store"
```

## Inicialización de la Aplicación Flask

Se crea una instancia de la aplicación Flask mediante `app = Flask(__name__)`.

## Conexión a la Base de Datos

Se utiliza Flask-MySQLdb para integrar MySQL con la aplicación Flask. Se verifica la conexión a la base de datos antes de ejecutar la aplicación mediante la creación de un cursor y la ejecución de una consulta de prueba.

```python
try:
    # Verifica la conexión a la base de datos antes de ejecutar la aplicación
    with app.app_context():
        db = mysql.connection
        cursor = db.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        print("Conexión a la base de datos establecida correctamente.")
except Exception as e:
    print("Error de conexión a la base de datos:", e)
```

## Realización del Login

### 1. Verificación de la Conexión a la Base de Datos

Primero, en el archivo `app.py`, se verifica la conexión a la base de datos antes de ejecutar la aplicación Flask. Esto se realiza utilizando el paquete `flask_mysqldb`. La verificación incluye la ejecución de una simple consulta para asegurarse de que la conexión sea exitosa.

```python
try:
    with app.app_context():
        db = mysql.connection
        cursor = db.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        print("Conexión a la base de datos establecida correctamente.")
except Exception as e:
    print("Error de conexión a la base de datos:", e)
```

### 2. Realización del Login

En la función `login` de `app.py`, se implementa el proceso de inicio de sesión. Se crea una instancia del usuario con los datos proporcionados en el formulario y se utiliza el método `login` del modelo `ModelUsers` para verificar la identidad del usuario.

```python
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            user = User(0, request.form['username'], request.form['password'], 0)
            print("Intento de inicio de sesión para el usuario:", user.username)
            
            with app.app_context():
                logged_user = ModelUsers.login(mysql, user)
            
            print("Usuario autenticado:", logged_user)
            
            if logged_user is not None:
                if logged_user.usertype == 1:
                    return redirect(url_for("admin"))

```
### 3. Manejo de Excepciones

Dentro de la función `login`, se manejan diferentes excepciones para proporcionar mensajes de error significativos. Esto incluye excepciones específicas para contraseñas incorrectas y problemas de interacción con la base de datos.
```
                else:
                    return redirect(url_for("home"))
            else:
                print("Acceso rechazado. Verifica tu nombre de usuario y contraseña.")
                flash("Acceso rechazado. Verifica tu nombre de usuario y contraseña.", 'error')
                return render_template("auth/login.html")
        except ValueError as ve:
            print("Contraseña incorrecta:", ve)
            flash("Contraseña incorrecta. Verifica tu nombre de usuario y contraseña.", 'error')
            return render_template("auth/login.html")
        except Exception as e:
            print("Error al interactuar con la base de datos:", e)
            flash("Ocurrió un error durante el inicio de sesión. Por favor, inténtalo nuevamente.", 'error')
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")
```
