# views.py
from django.http import JsonResponse

def store_api(request):
    # Your API logic here
    data = {'message': 'This is the store API endpoint'}
    return JsonResponse(data)
