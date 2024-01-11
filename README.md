# CasoPracticoZEPO-3

## Proposito y alcance del proyecto

Haciendo uso de Python o de algún framework de desarrollo basado en Python (como por ejemplo DRF), realizar una clase que simule un ataque de diccionario a una contraseña probando una lista de contraseñas de uso común y sus variaciones.

- common_passwords = ["password", "password123", "letmein", "qwerty", "123456", "abc123", "admin", "welcome", "monkey", "sunshine"]

- password_variations = ["", "123", "1234", "12345", "123456", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "<", ">"]

## Herramientas y tecnologías utilizadas

- Python
- DRF (Django REST Framework)

## Implementacion

- password_attack/urls.py (proyecto): Se configura como se deben manejar las URLs del proyecto. 
- password_cracker/views.py: Se implementa una vista que contiene una clase para realizar el ataque de diccionario en una contraseña objetivo
- password_cracker/urls.py (aplicacion): Se configuran las URL de la aplicación. 

## Manual de usuario

### Configuracion del entorno virtual

Ya esta previamente creado el entorno virtual, simplemente hay que activarlo haciendo uso del comando 'source myenv/bin/activate'

### Instalar dependencias

Una vez iniciado el entorno, hay que instalar si no cuentas con ello django, para ello 'pip install django'.

### Iniciar

Antes de iniciarla hay que hacer la migracion, 'python3 manage.py migrate'. Para iniciar la aplicación, hay que ejecutar el comando 'python3 manage.py runserver'. Una vez iniciado el programa ya podemos acceder a la URL para realizar el ataque de diccionario, la URL es la siguiente: http://127.0.0.1:8000/password_attack/test_password/password/