from dataclasses import field, fields
from pickletools import read_bytes4
from pyexpat import model
from rest_framework import serializers
from .models import Question,Answer

class QuestionSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    slug   = serializers.SlugField(read_only=True)
    class Meta:
        model = Question
        fields = '__all__'
class AnswerSerializer(serializers.ModelSerializer):
    author   = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Answer
        # fields = '__all__'
        exclude = ['question']
