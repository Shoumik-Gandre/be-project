from django.shortcuts import render


# Create your views here.
def index(request):
    word_list = [
        'The misanthrope did not like wars',
        'Earlier on, he realised the flaws in society',
        'Peace was never an option',
        'The car was big',
        'The care was big'
    ]
    context = {
        'word_list': word_list,
        'text': ''
    }
    return render(request, 'jaishruti/index.html', context)
