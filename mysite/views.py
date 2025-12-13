import socket
from django.http import JsonResponse


def ping(request):
    return JsonResponse({
        "status": "ok",
        "hostname": socket.gethostname()
    })
