from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pokemon.crawler import get_poke
from pokemon.models import Name


@csrf_exempt
def url_input(request):
    """
    :return:
    """
    if request.method == "POST":
        try:
            response = get_poke()
            data = {
                   'id': response['id'],
                   'name': response['name'],
                   'characteristics': {
                       'abilities': response['abilities'],
                       'height': response['height'],
                       'weight': response['weight']
                   }
                }
            N = Name(
                id=data['id'],
                name=data['name'],
                height=data['characteristics']['height'],
                weight=data['characteristics']['weight'],
                date=timezone.now()
            )
            N.save()
            return JsonResponse(data)
        except Exception as e:
            data = {
                "success": False,
                "data": {"Error Url Input Function" + e}
            }
        return JsonResponse(data)
    else:
        data = {
            "success": False,
            "data": "Error Request Request"
        }
        print(data)
        return JsonResponse(data)



