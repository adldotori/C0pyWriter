from django.shortcuts import render
from gpt2.src.interactive_conditional_samples import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def complete(request):
    if request.method == "POST":
        text = request.POST.get('text')
        return JsonResponse(interact_model(raw_text=text))


@csrf_exempt
def summary(request):
    if request.method == "POST":
        text = request.POST.get('text')
        text = text + '\nTL;DR:'
        return JsonResponse(interact_model(raw_text=text))