from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse 
from rest_framework.renderers import JSONRenderer
# Create your views here.

def student_detailone(request, pk):
    stu = Student.objects.get(id=pk)
    # print(stu)
    serializer = StudentSerializer(stu)
    #print(serializer)
    #print(serializer.data)
    #######
    ###############json_data = JSONRenderer().render(serializer.data)
    #######
    #print(json_data)
    #######we may use just one line which is at the last in place of these two lines
    ###############return(HttpResponse(json_data, content_type = 'application/json'))
    #######
    return JsonResponse(serializer.data)
    # if we have serializer.data which is not dict object then we have to write
    # return JsonResponse(serializer.data, safe = 'False')

def student_details(request):
    stu = Student.objects.all()
    # print(stu)
    serializer = StudentSerializer(stu, many='true')
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return(HttpResponse(json_data, content_type = 'application/json'))