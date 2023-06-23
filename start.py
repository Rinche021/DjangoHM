import os

project_name = input("Введите название каталога в котором находится файл manage.py: ")
os.system(f"cd {project_name}")
os.system("python manage.py runserver")