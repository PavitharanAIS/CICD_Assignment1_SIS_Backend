from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, StudentSerializer, ProgrammeSerializer, LecturerSerializer, MarksSerializer, \
    TuitionFeeSerializer
from rest_framework.permissions import AllowAny, AllowAny
from .models import Student, Programme, Lecturer, Marks, TuitionFee


class StudentListCreate(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        return Student.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


class StudentDelete(generics.RetrieveDestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return Student.objects.all()


class ProgrammeListCreate(generics.ListCreateAPIView):
    serializer_class = ProgrammeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        ids = self.request.query_params.get('ids')
        if ids:
            ids = list(map(int, ids.split(',')))
            return Programme.objects.filter(id__in=ids)
        return Programme.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


class ProgrammeDelete(generics.RetrieveDestroyAPIView):
    serializer_class = ProgrammeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return Programme.objects.all()


class LecturerListCreate(generics.ListCreateAPIView):
    serializer_class = LecturerSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        ids = self.request.query_params.get('ids')
        if ids:
            ids = list(map(int, ids.split(',')))
            return Lecturer.objects.filter(id__in=ids)
        return Lecturer.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


class LecturerDelete(generics.RetrieveDestroyAPIView):
    serializer_class = LecturerSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        # Double check here 41:13
        return Lecturer.objects.all()


class MarksListCreate(generics.ListCreateAPIView):
    serializer_class = MarksSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        ids = self.request.query_params.get('ids')
        if ids:
            ids = list(map(int, ids.split(',')))
            return Marks.objects.filter(id__in=ids)
        return Marks.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


class MarksDelete(generics.RetrieveDestroyAPIView):
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

        ids = self.request.query_params.get('ids')
        if ids:
            ids = list(map(int, ids.split(',')))
            return TuitionFee.objects.filter(id__in=ids)
        return TuitionFee.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)


class TuitionFeeDelete(generics.RetrieveDestroyAPIView):
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
