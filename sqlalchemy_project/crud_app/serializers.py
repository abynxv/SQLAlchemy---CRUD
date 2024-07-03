from rest_framework import serializers
from .models import College, Student
from .sqlalchemy_config import get_db


class CollegeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=255)

    def create(self, validated_data):
        db = next(get_db())
        college = College(**validated_data)
        db.add(college)
        db.commit()
        db.refresh(college)
        return college

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        db = next(get_db())
        db.commit()
        db.refresh(instance)
        return instance

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    college_id = serializers.IntegerField()

    def create(self, validated_data):
        db = next(get_db())
        student = Student(**validated_data)
        db.add(student)
        db.commit()
        db.refresh(student)
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.college_id = validated_data.get('college_id', instance.college_id)
        db = next(get_db())
        db.commit()
        db.refresh(instance)
        return instance
    
