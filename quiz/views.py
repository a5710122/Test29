from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Question, Choice, User
from django.utils import timezone

def index(request):
    """ show question 10 sort by pubiher date """
    latest_question_list = Question.objects.order_by('pub_date')[:10]    
    return render(request, 'quiz/index.html', {'latest_question_list': latest_question_list})

  
def detail(request, question_id):
    """ show choice of question """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})


def results(request, question_id):
    """ show number people ans of question """
    question = get_object_or_404(Question, pk=question_id)
    
    #user_from_db = User.objects.values('user_point', 'username')
    user_from_db = User.objects.get(name='Silver')
    print(user_from_db.username)
    return render(request, 'quiz/results.html', {'question': question, 'username_show_html' : user_name})


def add_question(request):
    """ add question to database """
    new_text_question = "No Question add to database"
    new_text_choice1 = "No Choice add to database"
    new_text_choice2 = "No choice add to database"
    choice1_true_false = ""
    choice2_true_false = ""
    
    #pass value from html to control (python)
    if request.method == 'POST':
       new_text_question = request.POST['new_text_question']
       new_text_choice1 = request.POST['new_text_choice1']
       new_text_choice2 = request.POST['new_text_choice2']
       choice1_true_false = request.POST['choice1']
       choice2_true_false = request.POST['choice2']
       
       #add question
       q = Question(question_text= new_text_question, pub_date=timezone.now())
       q.save()
       q.choice_set.create(choice_text=new_text_choice1, ans=choice1_true_false, votes=0)
       q.choice_set.create(choice_text=new_text_choice2, ans=choice2_true_false, votes=0)
    
       
    # pass value form control (python) to html
    show_question = { 
                   'quest_text'   : new_text_question,
                   'choice1_text' : new_text_choice1,
                   'choice2_text' : new_text_choice2,
                   'choice1_true_false' : choice1_true_false,
                   'choice2_true_false' : choice2_true_false 
    }
    return render(request,'quiz/add_question.html',show_question )


def vote(request, question_id):
    """ count number of ans """
    username_now = ''
    point_now = 0
    question = get_object_or_404(Question, pk=question_id)
    try:
        if request.method == 'POST':
           username_now = request.POST['username']

           if (User.objects.filter(username = username_now)):
              user = User.objects.get(username = username_now)
              user.username = username_now 
              user.save()
           else:
              user = User(username=username_now, user_point=0)
              user.save()

        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        check_ans = question.choice_set.get(choice_text = selected_choice)
        check_true_false = question.choice_set.get(ans ='True')
        user = User.objects.get(username = username_now)
        print(check_ans)
        print(check_true_false)
        print(user)

        if(check_ans == check_true_false):
           user.user_point += 1
           user.save() 
        else:
           user.user_point += 0
           user.save()
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
