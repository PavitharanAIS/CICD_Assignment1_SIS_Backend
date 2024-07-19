from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, StudentSerializer, ProgrammeSerializer, LecturerSerializer, MarksSerializer, \
    TuitionFeeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Student, Programme, Lecturer, Marks, TuitionFee


class StudentListCreate(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return Student.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


class StudentDelete(generics.DestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return Student.objects.all()


class ProgrammeListCreate(generics.ListCreateAPIView):
    serializer_class = ProgrammeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return Programme.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


class ProgrammeDelete(generics.DestroyAPIView):
    serializer_class = ProgrammeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return Programme.objects.all()


class LecturerListCreate(generics.ListCreateAPIView):
    serializer_class = LecturerSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return Lecturer.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


class LecturerDelete(generics.DestroyAPIView):
    serializer_class = LecturerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return Lecturer.objects.all()


class MarksListCreate(generics.ListCreateAPIView):
    serializer_class = MarksSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return Marks.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


class MarksDelete(generics.DestroyAPIView):
    serializer_class = MarksSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return Marks.objects.all()


class TuitionFeeListCreate(generics.ListCreateAPIView):
    serializer_class = TuitionFeeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return TuitionFee.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


class TuitionFeeDelete(generics.DestroyAPIView):
    serializer_class = TuitionFeeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return TuitionFee.objects.all()


#Creating View for User Registration
class CreateUserView(generics.CreateAPIView):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return User.objects.all()
