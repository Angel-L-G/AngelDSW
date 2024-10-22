//Crear Proyecto
python -m venv .venv --prompt <Nombre proy>

//Activar entorno virtual
source .venv/bin/activate

//Instalar django
pip install django

//Crear proyecto
django-admin startproject <Nombre Proy> .
(Importante el punto)

//ver comandos
./manage.py

//Levantar server
./manage.py runserver

//Crear aplicacion
./manage.py startapp <Nombre app>
