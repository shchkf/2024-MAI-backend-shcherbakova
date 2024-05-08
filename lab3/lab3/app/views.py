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
def change_rating(request, film_id, user_id):
    return JsonResponse({'rating': 'not changed'})
    # if film_id is None or user_id is None:
    #     return HttpResponseBadRequest({'error': 'cosmetic or user id is missing'})
    # current_user = User.objects.get(pk=user_id)
    # current_cosmetic= Cosmetic.objects.get(pk=film_id)
    # if request.method == "PUT":
    #     rate = int(json.loads(request.body)['rate'])
    #     old_rate = Rating.objects.get(user_id=current_user, film_id=current_cosmetic)
    #     rate_delta = rate - old_rate['summ_rating']
    #     old_rate.update(summ_rating=rate)
    #     summ_rating = ['summ_rating'] + rate_delta
    #     current_cosmetic.update(summ_rating=summ_rating)
    #     return JsonResponse({'status': "ok"})
    # elif request.method == "POST":
    #     rate = int(json.loads(request.body)['rate'])
    #     Rating.objects.create(user_id=current_user, film_id=current_cosmetic, rate=rate)
    #     rating = current_cosmetic['rating'] + rate
    #     count_rating = current_cosmetic['count_rating'] + 1
    #     current_cosmetic.update(rating=rating, count_rating=count_rating)
    #     return JsonResponse({'status': "ok"})


