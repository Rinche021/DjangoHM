import os

virtual_name = input("Название виртуального окружения: ")
os.system(f"python -m venv {virtual_name}")
os.system(f"{virtual_name}/Script/activate")
