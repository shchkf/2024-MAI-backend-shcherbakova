import json

from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Cosmetic, User, Rating


@csrf_exempt
@require_http_methods(['GET'])
def cosmetics(request):
    return JsonResponse({'cosmetics':'no'})
    # cosmetic_objects = Cosmetic.objects.all()
    # return JsonResponse({'cosmetics': [model_to_dict(cosmetic) for cosmetic in cosmetic_objects]})


@csrf_exempt
@require_http_methods(['GET'])
def users(request):
    return JsonResponse({'users': 'no'})
    # cosmetic_objects = User.objects.all()
    # return JsonResponse({'users': [model_to_dict(cosmetic) for cosmetic in cosmetic_objects]})


@csrf_exempt
@require_http_methods(['GET'])
def user(request, user_id):
    if request.method == "GET":
        return JsonResponse({'user': 'no'})
        # current_user = User.objects.get(pk=user_id)
        # return JsonResponse({'user': model_to_dict(current_user)})

@csrf_exempt
@require_http_methods(['POST'])
def add_user(request):
    if request.method == 'POST':
        return JsonResponse({'user': 'no added'})
        # post_data = json.loads(request.body.decode("utf-8"))
        # User.objects.create(login=post_data['login'], password=post_data['password'], fio=post_data['fio'])
        # return JsonResponse({'status': 'ok'})


@csrf_exempt
@require_http_methods(['POST'])
def add_cosmetic(request):
    if request.method == 'POST':
        return JsonResponse({'cosmetic': 'no added'})
        # post_data = json.loads(request.body.decode("utf-8"))
        # Cosmetic.objects.create(name=post_data['name'], type=post_data['type'], country=post_data['country'],
        #                         rating=post_data['value_rating'], count_rating=post_data['count_rating'], description=post_data['description'])
        # return JsonResponse({'status': 'ok'})

@csrf_exempt
@require_http_methods(['GET'])
def cosmetic(request, cosmetic_id):
    if request.method == "GET":
        return JsonResponse({'cosmetic': 'no'})
        # current_user = Cosmetic.objects.get(pk=film_id)
        # return JsonResponse({'cosmetic': model_to_dict(current_user)})



@csrf_exempt
@require_http_methods(['PUT', 'POST'])
def change_rating(request, cosmetic_id, user_id):
    return JsonResponse({'rating': 'not changed'})



