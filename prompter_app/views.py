from django.shortcuts import render
from .models import Prompt, Playwright

# Create your views here.

def prompt_list(request):
    prompts = Prompt.objects.all()
    return render(request, 'prompt/prompt_list.html', {'prompts': prompts})


    # from django.http import JsonResponse

# def my_view(request):
    # questions = Question.objects.all()
    # return JsonResponse({'questions': questions})