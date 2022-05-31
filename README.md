# Instrucciones para ejecutar este proyecto


Clonar el proyecto

git clone https://github.com/waltervd9512/entrega.git

cd .\entrega\
cd .\BibliotecaWeb\   

Crear base de datos con los Modelos (hacer migraciones y migrar)

py .\manage.py makemigrations


py .\manage.py sqlmigrate app_biblioteca 0001   


py .\manage.py migrate  



Crear base de datos con los Modelos (hacer migraciones y migrar)
python manage.py makemigrations app_coder

python manage.py migrate
Crear super-usuario
python manage.py createsuperuser
Ejecutar proyecto
python manage.py runserver
