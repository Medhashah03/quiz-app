from django.shortcuts import render, HttpResponse ,redirect
from django.http import JsonResponse
from .models import *
import random
from .serializers import QuestionSerializer,AnswerSerializer

from rest_framework import generics
# from django import template
def quiz(request):
    return render(request,'quiz.html') 

def home(request):
    categories = Category.objects.all()
    #questions = Question.objects.all()
    context = {'categories': categories}
    question_objs = Question.objects.all()
    answer_objs = Answer.objects.all()
    if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))   
            return render(request,'quiz.html',{"questionSet" :question_objs})
    
   
        
    return render(request,'index.html',context)


def viewCategories(request):
    return HttpResponse("Hello From Django")

# def get_quiz(request):
#     try:
#         # Converting to list to use shuffle on it
#         question_objs = Question.objects.all()
#         if request.GET.get('category'):
#             question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))
    
#         #question_objs= list(question_objs)
        
#         data = []
#         #random.shuffle(question_objs)
#         for question_obj in question_objs:
           
#             data.append({
#                 "category" : question_obj.category.category_name,
#                 "question" : question_obj.question,
#                 "marks": question_obj.marks,
#                 "answers": question_obj.get_answers()
#             })

#         payload = {'status': True, 'data' : data}


#         return JsonResponse(payload)

#     except Exception as e:
#             print(e)
#     return HttpResponse("Somethings Wrong")




# def check_answer(request):
#     score =0
#     if request.method == 'POST':
#         selected_answer = request.POST.get('answer')
#         answerobj = Answer.objects.filter(answer__icontains=selected_answer)
#         answer_value = answerobj[0]
#         for answer in Answer.objects.all():
#             if answer==answer_value:
#                 if answer.is_correct:
#                     score =score+5
#     context = {'score':score}
#     return render(request,'scoreCard.html',context)

def check_answer(request):
    score = 0

    if request.method == 'POST':
        selected_answer = request.POST.get('answer')
        answerobj = Answer.objects.filter(answer__icontains=selected_answer, is_correct=True).first()
        
        if answerobj is not None:
            score += 5

    context = {'score': score}
    return render(request, 'scoreCard.html', context)





class QuestionAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


  

