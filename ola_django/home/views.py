from django.shortcuts import render


def home(request):
    context = {
                'text': 'Estou na home'
            }

    return render(request,
                  'home/index.html',
                  context
    )
