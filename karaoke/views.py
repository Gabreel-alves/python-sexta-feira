from django.shortcuts import render

# Create your views here.
    context = {'nome' :[
        'gabrieu',
        'bruno',
        'camila'
        ], 
        'vazio' : False
        'teste' : 'teste'
        }
        return render(request, 'index.hmtl',context)

def index(request): 
    return render(request, 'index.html',{'minhavar' : '2'})
