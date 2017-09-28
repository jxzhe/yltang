from django.shortcuts import render

def main(request):
    context = {'like': 'Django很棒'}
    return render(request, 'main/main.html', context)

def about(request):
    context = {'range10': range(10)}
    return render(request, 'main/about.html', context)