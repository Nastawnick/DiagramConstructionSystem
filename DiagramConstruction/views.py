from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def test(request):
    return JsonResponse({'response': 'success'})

def main(request):
    return render(request=request, template_name='base.html')