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
        result = interact_model(raw_text=text, length=min(len(text) // 10, 100))
        try:
            result = result.split('|endoftext|')[0]
        except:
            pass
        return Response({'text': result})


@csrf_exempt
@api_view(['POST'])
def summary(request):
    if request.method == "POST":
        text = request.data['text']
        text = text + '\nTL;DR:'
        result = interact_model(raw_text=text, length=min(len(text) // 10, 100))
        try:
            result = result.split('|endoftext|')[0]
        except:
            pass
        return Response({'text': result})