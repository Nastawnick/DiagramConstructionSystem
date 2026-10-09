from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.
def main(request):
    return JsonResponse({'response': 'success'})
