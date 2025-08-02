from rest_framework import generics

from .models import Question
from .serializers import QuestionSerializer


class PollList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class PollDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
