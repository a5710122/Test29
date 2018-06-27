from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Question, Choice


def index(request):
    """ show question 5 sort by pubiher date """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'quiz/index.html', context)

  
def detail(request, question_id):
    """ show choice of question """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})


def results(request, question_id):
    """ show number people ans of question """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/results.html', {'question': question})


def add_question(request):
    """ add question to database """
    question = get_object_or_404(Question, pk=question_id)
    new_text_question = "No Question add to database"
    new_text_choice1 = "No Choice add to database"
    new_text_choice2 = "No choice add to database"
    
    if request.method == 'POST':
       new_text_question = request.POST['new_text_question']
       new_text_choice1 = request.POST['new_text_choice1']
       new_text_choice2 = request.POST['new_text_choice2']
       choice1 = request.POST['choice1']
       choice2 = request.POST['choice2']
    show_question = { 
                   'quest_text'   : new_text_question,
                   'choice1_text' : new_text_choice1,
                   'choice2_text' : new_text_choice2,
                   'choice1_true_false' : choice1,
                   'choice2_true_false' : choice2
    }
    return render(request,'quiz/add_question.html',show_question )

#def add_check_choice(request):
        



def vote(request, question_id):
    """ count number of ans """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'quiz/no_ans_quiz.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('quiz:results', args=(question.id,)))
