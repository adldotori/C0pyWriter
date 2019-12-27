from django.shortcuts import render
from gpt2.src.interactive_conditional_samples import *
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(['POST'])
def complete(request):
    if request.method == "POST":
        text = request.data['text']
        return Response({'text': interact_model(raw_text=text)})


@csrf_exempt
@api_view(['POST'])
def summary(request):
    if request.method == "POST":
        text = request.data['text']
        text = text + '\nTL;DR:'
        return Response({'text': interact_model(raw_text=text)})