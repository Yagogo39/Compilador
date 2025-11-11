from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json
#importamos nuestro metodo
from api.utils import run_code

@api_view(['POST'])

def main(request):

    if request.method != 'POST':
        return JsonResponse(
            {'code':''},
            status=405
        )
    #Parseamos el cuerpo de la peticion en JSON
    try:
        body = request.body.decode('utf-8') if request.body else ''
        data = json.loads(body) if body else {}
    except Exception as e:
        return JsonResponse(
            {'code':''},
            status=405
        )
    
    #De JSON obtenemos el que tiene texto
    code = data.get('text','')
    #Ejecutamos las instrucciones con el metodo que definimos.
    output = run_code(code)
    #De una respuesta de tipo JSON
    return Response(
        {"output":output},
        status=status.HTTP_200_OK
    )