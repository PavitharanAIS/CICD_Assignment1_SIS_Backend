from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Student, Programme, Lecturer, Marks, TuitionFee


# Creating serializer for User Registration
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "roll", "address", "programme", "tuitionFee", "lecturer", "attendance", "marks",
                  "created_at", "updated_at"]


class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = ["id", "name", "duration", "created_at", "updated_at"]


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ["id", "name", "lecturer_programme", "created_at", "updated_at"]


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = ["id", "programmeMarks", "created_at", "updated_at"]


class TuitionFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuitionFee
        fields = ["id", "programme", "tuitionFee", "created_at", "updated_at"]
