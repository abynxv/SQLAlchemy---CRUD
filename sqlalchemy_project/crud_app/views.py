from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import College, Student
from .serializers import CollegeSerializer, StudentSerializer
from .sqlalchemy_config import get_db

@api_view(['GET', 'POST'])
def college_list(request):
    db = next(get_db())
    if request.method == 'GET':
        colleges = db.query(College).all()
        serializer = CollegeSerializer(colleges, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def college_detail(request, pk):
    db = next(get_db())
    college = db.query(College).filter(College.id == pk).first()
    if college is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CollegeSerializer(college)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CollegeSerializer(college, data=request.data)
        if serializer.is_valid():
            college.name = serializer.validated_data.get('name', college.name)
            college.address = serializer.validated_data.get('address', college.address)
            db.commit()
            db.refresh(college)
            updated_serializer = CollegeSerializer(college)
            return Response(updated_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        db.delete(college)
        db.commit()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def student_list(request):
    db = next(get_db())
    if request.method == 'GET':
        students = db.query(Student).all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    db = next(get_db())
    student = db.query(Student).filter(Student.id == pk).first()
    if student is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            student.name = serializer.validated_data.get('name', student.name)
            student.age = serializer.validated_data.get('age', student.age)
            student.college_id = serializer.validated_data.get('college_id', student.college_id)
            db.commit()
            db.refresh(student)
            updated_serializer = StudentSerializer(student)
            return Response(updated_serializer.data)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        db.delete(student)
        db.commit()
        return Response(status=status.HTTP_204_NO_CONTENT)
