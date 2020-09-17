"""OnlineQuizPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Accounts import views as acc_views
from ExamManagement import views as exam_views
from OnlineQuiz import views
from ResultManagement import views as result_views
from AnswerManagement import views as answer_views


urlpatterns = [
    path('', views.showHome),
    path('login/', acc_views.login_view),
    path('signup/', acc_views.register_view),
    path('logout/', acc_views.logout_view),
    path('dashboard/', acc_views.user_dash),
    path('admin/', admin.site.urls),
    path('exams/', exam_views.showExams, name='exams'),
    path('attexams/', exam_views.showAttemptedExam, name='attempt_exams'),
    path('results/', result_views.showResults, name='results'),
    path('history/', result_views.showExaminee_History, name='history'),
    path('rank/', result_views.showRank, name='rank'),
    path('mcqanswer/', answer_views.showMcqAnswer, name='mcqanswer'),
    path('cusquestion/',exam_views.showCustomQuestions, name='cusquestion'),
    path('question/', exam_views.showQuestions, name='question'),
    path('mcqquestion/', exam_views.showMCQQuestions, name='mcqquestion'),
    path('answer/', answer_views.showAnswer, name='answer'),
    path('cusanswer/', answer_views.showCustomAnswer, name='cusanswer'),



]
