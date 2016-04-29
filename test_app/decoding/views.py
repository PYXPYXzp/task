# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

import coding


def index(request):
    return render(request, 'decoding/main.html')


def decode_text(request):
    result = ''
    if request.method == 'POST':
        method = request.POST.get('type')  # Тип выполняемой операции
        text = request.POST.get('text')
        shift = request.POST.get('shift')
        if coding.is_valid_request(text, shift):
            if method == 'decode':
                result = coding.encoding(text, -int(shift))
            elif method == 'encode':
                result = coding.encoding(text, shift)
        else:
            return HttpResponse(status=400)
    return JsonResponse(result)


def change_text(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        count_letter = coding.letter_count(text)
        return JsonResponse(count_letter)
