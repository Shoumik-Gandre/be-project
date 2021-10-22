from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import PronuanceWords
import os


# Create your views here.
def index(request):
    query = "select words_id,words from pronuance_words where wordlength=5 and words like 'c%' limit 5"
    wordslist = PronuanceWords.objects.all().raw(query)
    # module_dir = os.path.dirname(__file__)  
    # file_path = os.path.join(module_dir, 'data.txt')   #full path to text.
    # data_file = open(file_path , 'r')       
    # data = data_file.read()
    context = {'wordslist': wordslist, 'text': ''}
    return render(request, 'index.html', context)
