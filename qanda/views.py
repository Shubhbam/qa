from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .models import Question,Answer
from .serializers import QuestionSerializers,AnswerSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor
# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsAuthor]
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

# class AnswerCreate(generics.CreateAPIView):
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer
#     def perform_create(self, serializer):
#         # return super().perform_create(serializer)
#         user     = self.request.user
#         slug     = self.kwargs.get('slug')
#         question = get_object_or_404(Question,slug=slug)
#         serializer.save(author = user,answers=question) 

# class AnswerList(generics.ListAPIView):
#     serializer_class = AnswerSerializer
#     def get_queryset(self):
#         slug    =    self.kwargs.get('slug')
#         return Answer.objects.filter(question__slug==slug)

class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        user = self.request.user
        slug = self.kwargs.get('slug')
        permission_classes = [IsAuthenticated]

        question = get_object_or_404(Question, slug=slug)
        serializer.save(author = user, question=question)


class AnswerList(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug=slug)

class AnswerDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

# class AnswerCreate(generics.CreateAPIView):
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer
#     # permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         user = self.request.user
#         slug = self.kwargs.get('slug')
#         question = get_object_or_404(Question, slug=slug)
#         serializer.save(author = user, question=question)


# class AnswerList(generics.ListAPIView):
#     serializer_class = AnswerSerializer
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         slug = self.kwargs.get('slug')
#         return Answer.objects.filter(question__slug=slug)
