# Instrucciones para ejecutar este proyecto


Clonar el proyecto

git clone https://github.com/waltervd9512/preentrega_coder.git

cd .\preentrega_coder\

cd .\BibliotecaWeb\   

Crear base de datos con los Modelos (hacer migraciones y migrar)

py .\manage.py makemigrations


py .\manage.py sqlmigrate app_biblioteca 0001   


py .\manage.py migrate  



Crear base de datos con los Modelos (hacer migraciones y migrar)
python manage.py makemigrations app_coder


py manage.py runserver
