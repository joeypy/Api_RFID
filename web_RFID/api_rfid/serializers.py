from rest_framework.serializers import ModelSerializer
from .models import Student

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        #fields = ('id', 'name', 'code', 'status')