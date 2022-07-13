import requests
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pokemon.crawler import crawler
from pokemon.models import Name


@csrf_exempt
def url_input(request):
    if request.method == "POST":
        try:
            crawler()
        except Exception as e:
            data = {
                "success": False,
                "data": {"Error Url Input Function:", e}
            }
            return JsonResponse(data)
        else:
            data = {
                "success": False,
                "data": "Error Request Request"
            }
            return JsonResponse(data)



