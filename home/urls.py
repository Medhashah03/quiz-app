
from django.urls import path
from . import views
from home.views import QuestionAPIView,viewCategories
urlpatterns = [
    path('', views.home, name="home"),
    path('api/get-quiz/', views.get_quiz, name="get_quiz"),
    path('api/get-category/', views.viewCategories, name="get_category"),
    path('api/questions/', QuestionAPIView.as_view(), name='questions'),
    path('quiz',views.quiz, name='quiz'),
    path('check-answer/', views.check_answer, name='check_answer'),
]
