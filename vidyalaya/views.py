from django.shortcuts import render



def index(request):
    latest_question_list = [1]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'home.html', context)
