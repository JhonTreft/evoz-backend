from .imports.index import * 
from apps.helpers.structure_folders.index import *

@csrf_exempt
@require_POST
def create_react_project(request):
    try:
        # Nombre del proyecto React (puedes pasarlo como parámetro POST)
        data = json.loads(request.body.decode('utf-8'))
        status_data = data.get("project")

        if status_data:
            project_name = status_data.get("name")
            # Ruta raíz script JS
            project_path_scripts = '/home/treft/Programacion_Entorno_Linux/React'
            os.chdir(project_path_scripts)

            # Ejecutar el script para crear el proyecto React
            process = subprocess.Popen(['node', 'run_npx.js', project_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

            # Función para enviar actualizaciones de estado al cliente
            def generate():
                yield json.dumps({'message': 'Starting project creation...', 'status': status_codes["OK"]}) + '\n'
                
                # Leer la salida estándar y la salida de error línea por línea y enviarlas al cliente
                for line in process.stdout:
                    yield json.dumps({'message': line.strip(), 'status': status_codes["OK"]}) + '\n'

                for line in process.stderr:
                    yield json.dumps({'message': line.strip(), 'status': status_codes["Bad_Request"]}) + '\n'

                # Esperar a que el proceso hijo termine y obtener el código de retorno
                return_code = process.wait()

                # Si el proceso hijo devuelve un código de error, lanzar una excepción
                if return_code != 0:
                    error_message = process.stderr.read().strip()
                    raise Exception(error_message)

                # Agregar mensaje de estructuración del proyecto
                yield json.dumps({'message': 'Structuring project...', 'status': status_codes["OK"]}) + '\n'

                # Organizar la estructura del proyecto
                project_path = f'/home/treft/Programacion_Entorno_Linux/React/{project_name}'
                organize_project(project_path, src_structure)

                yield json.dumps({'message': 'Project created successfully', 'status': status_codes["OK"]}) + '\n'

            # Devolver una respuesta de transmisión que envíe actualizaciones de estado al cliente
            return StreamingHttpResponse(generate(), content_type='application/json')

    except Exception as e:
        return JsonResponse({'error': str(e), 'status_code': status_codes["Bad_Request"]}, status=status_codes["Bad_Request"])    
    except OSError as e:
        return JsonResponse({'error': f'Error al crear el proyecto: {str(e)}','status_code':status_codes["Bad_Request"]}, status=status_codes["Bad_Request"])


"""
@csrf_exempt
@require_POST
def create_react_project(request):
    try:
        # Nombre del proyecto React (puedes pasarlo como parámetro POST)
        data = json.loads(request.body.decode('utf-8'))
        status_data = data.get("project")

        if status_data:
            project_name = status_data.get("name")
            #Ruta raiz script JS
            project_path_scripts = '/home/treft/Programacion_Entorno_Linux/React'
            os.chdir(project_path_scripts)
            
            subprocess.run(['node', 'run_npx.js', project_name], check=True)


            # Ruta donde se creará el proyecto React
            project_path = f'/home/treft/Programacion_Entorno_Linux/React/{project_name}'

            # Cambiar al directorio del proyecto
            os.chdir(project_path)

            # Ejecutar el comando para crear el proyecto React

            organize_project(project_path, src_structure)
            # Devolver una respuesta JSON
            return JsonResponse({'message': 'project created OK', 'status': status_codes["OK"]}, status=status_codes["OK"])    
    except Exception as e:
        return JsonResponse({'error': str(e), 'status_code': status_codes["Bad_Request"]}, status=status_codes["Bad_Request"])    
    except OSError as e:
        return JsonResponse({'error': f'Error al crear el proyecto: {str(e)}','status_code':status_codes["Bad_Request"]}, status=status_codes["Bad_Request"])
"""



@csrf_exempt
@require_POST
def create_django_project(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        project_name = data.get("project", {}).get("name")
        project_path_scripts = '/home/treft/Programacion_Entorno_Linux/Django'
        os.chdir(project_path_scripts)

        process = subprocess.Popen(['django-admin', 'startproject', project_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        def generate():
            yield json.dumps({'message': 'Starting Django project creation...', 'status': status_codes["OK"]}) + '\n'

            for line in process.stdout:
                yield json.dumps({'message': line.strip(), 'status': status_codes["OK"]}) + '\n'

            for line in process.stderr:
                yield json.dumps({'message': line.strip(), 'status': status_codes["Bad_Request"]}) + '\n'

            return_code = process.wait()
            if return_code != 0:
                error_message = process.stderr.read().strip()
                raise Exception(error_message)

            yield json.dumps({'message': 'Django project created successfully', 'status': status_codes["OK"]}) + '\n'

        return StreamingHttpResponse(generate(), content_type='application/json')

    except Exception as e:
        return JsonResponse({'error': str(e), 'status_code': status_codes["Bad_Request"]}, status=status_codes["Bad_Request"])


@csrf_exempt
@require_POST
def create_springboot_project(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        project_name = data.get("project", {}).get("name")
        project_path_scripts = '/home/treft/Programacion_Entorno_Linux/SpringBoot'
        os.chdir(project_path_scripts)

        process = subprocess.Popen(['spring', 'init', '--dependencies=web,data,jpa', project_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        def generate():
            yield json.dumps({'message': 'Starting Spring Boot project creation...', 'status': status_codes["OK"]}) + '\n'

            for line in process.stdout:
                yield json.dumps({'message': line.strip(), 'status': status_codes["OK"]}) + '\n'

            for line in process.stderr:
                yield json.dumps({'message': line.strip(), 'status': status_codes["Bad_Request"]}) + '\n'

            return_code = process.wait()
            if return_code != 0:
                error_message = process.stderr.read().strip()
                raise Exception(error_message)

            yield json.dumps({'message': 'Spring Boot project created successfully', 'status': status_codes["OK"]}) + '\n'

        return StreamingHttpResponse(generate(), content_type='application/json')

    except Exception as e:
        return JsonResponse({'error': str(e), 'status_code': status_codes["Bad_Request"]}, status=status_codes["Bad_Request"])


@csrf_exempt
@require_POST
def create_angular_project(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        project_name = data.get("project", {}).get("name")
        project_path_scripts = '/home/treft/Programacion_Entorno_Linux/Angular'
        os.chdir(project_path_scripts)

        process = subprocess.Popen(['ng', 'new', project_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        def generate():
            yield json.dumps({'message': 'Starting Angular project creation...', 'status': status_codes["OK"]}) + '\n'

            for line in process.stdout:
                yield json.dumps({'message': line.strip(), 'status': status_codes["OK"]}) + '\n'

            for line in process.stderr:
                yield json.dumps({'message': line.strip(), 'status': status_codes["Bad_Request"]}) + '\n'

            return_code = process.wait()
            if return_code != 0:
                error_message = process.stderr.read().strip()
                raise Exception(error_message)

            yield json.dumps({'message': 'Angular project created successfully', 'status': status_codes["OK"]}) + '\n'

        return StreamingHttpResponse(generate(), content_type='application/json')

    except Exception as e:
        return JsonResponse({'error': str(e), 'status_code': status_codes["Bad_Request"]}, status=status_codes["Bad_Request"])
