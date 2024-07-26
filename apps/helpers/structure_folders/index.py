import os
import shutil
from django.http import JsonResponse

def organize_project(project_path, src_structure):
    src_path = os.path.join(project_path, 'src')
    actions_path = os.path.join(src_path, 'actions')

    # Crear la carpeta 'actions' dentro de src
    os.makedirs(actions_path, exist_ok=True)

    # Crear las carpetas del src_structure dentro de 'actions'
    for folder_name, files in src_structure.items():
        folder_path = os.path.join(actions_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        # Mover los archivos a la carpeta correspondiente dentro de 'actions'
        for file in files:
            source = os.path.join(src_path, file)
            destination = os.path.join(folder_path, file)
            shutil.move(source, destination)
