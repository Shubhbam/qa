from django.db import router
from django.urls import URLPattern, path,include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet,AnswerCreate,AnswerList,AnswerDeleteUpdate

router = DefaultRouter()
router.register('question',QuestionViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('question/<slug:slug>/answercreate',AnswerCreate.as_view()),
    path('question/<slug:slug>/answer',AnswerList.as_view()),
    path('answer/<int:pk>/answer',AnswerDeleteUpdate.as_view()),
]