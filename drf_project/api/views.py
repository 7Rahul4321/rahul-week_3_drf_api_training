from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET', 'POST'])
def home(request):

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


@api_view(['PUT'])
def update_student(request, pk):

    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


@api_view(['DELETE'])
def delete_student(request, pk):

    student = Student.objects.get(id=pk)
    student.delete()

    return Response({"message": "Student deleted successfully"})
from django.contrib.auth.models import User
from .user_serializers import RegisterSerializer
@api_view(['POST'])
def register(request):

    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"})

    return Response(serializer.errors)
@api_view(['POST'])
def login(request):

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        return Response({"message": "Login successful"})

    return Response({"message": "Invalid credentials"})