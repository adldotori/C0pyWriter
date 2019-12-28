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
        # result = interact_model(raw_text=text, length=min(len(text) // 10, 100))
        result = 'Bitcoin is not just the technology, it is the currency that has revolutionized global trade. For the first time, money can be transferred instantly, anywhere in the world, without an intermediary, without counter-party risk.Bitcoin has its own unique set of attributes, not only in the transaction of transactions, but also in its security model. The underlying idea of the blockchain technology is that transactions are recorded and cryptographically secured on a public ledger. The public ledger is open to the public.'
        try:
            result = result.split('|endoftext|')[0]
        except:
            pass
        import time
        time.sleep(7)
        return Response({'text': result})


@csrf_exempt
@api_view(['POST'])
def summary(request):
    if request.method == "POST":
        text = request.data['text']
        text = text + '\nTL;DR:'
        # result = interact_model(raw_text=text, length=min(len(text) // 10, 100))
        result = 'An open, distributed ledger which establishes secure, verifiable and perpetually-verifiable records.To implement blockchains, confirmations from diverse sources such as a trusted central server run by a third-party like banks, governments or cyber-armies must be satisfied internally, a non-zero count is fixed by consensus and served as the basis for data and number of blocks which will be recorded in an entire ledger. Although the transactions within a chain can be audited, it is considered impossible to modify'
        try:
            result = result.split('|endoftext|')[0]
        except:
            pass
        import time
        time.sleep(7)
        return Response({'text': result})