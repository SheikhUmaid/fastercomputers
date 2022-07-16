from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SMS.serializer import StudentSerializer
from SMS.models import Student
# Create your views here.

@api_view(['GET'])
def getStudent(request):
    print(request.GET)
    id = request.GET["id"]
    print(id)
    student = Student.objects.filter(id=id)
    serializer = StudentSerializer(student, many = True)
    data = serializer.data
    return Response(data)
