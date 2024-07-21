from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Student, Programme, Lecturer, Marks, TuitionFee


class StudentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')
        self.programme = Programme.objects.create(name='Test Programme', duration='4 years')
        self.lecturer = Lecturer.objects.create(name='Test Lecturer', lecturer_programme=self.programme)
        self.marks = Marks.objects.create(programmeMarks='A')
        self.tuition_fee = TuitionFee.objects.create(programme=self.programme, fee='5000')
        self.student = Student.objects.create(
            name='Test Student',
            roll=1,
            address='123 Test St',
            programme=self.programme,
            tuitionFee=self.tuition_fee,
            lecturer=self.lecturer,
            attendance=95,
            marks=self.marks
        )

    def test_create_student(self):
        url = reverse('student-list')
        data = {
            'name': 'New Student',
            'roll': 2,
            'address': '456 New St',
            'programme': self.programme.id,
            'tuitionFee': self.tuition_fee.id,
            'lecturer': self.lecturer.id,
            'attendance': 85,
            'marks': self.marks.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)

    def test_list_students(self):
        url = reverse('student-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_student(self):
        url = reverse('student-delete', kwargs={'pk': self.student.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 0)


class ProgrammeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')
        self.programme = Programme.objects.create(name='Test Programme', duration='4 years')

    def test_create_programme(self):
        url = reverse('programme-list')
        data = {'name': 'New Programme', 'duration': '3 years'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Programme.objects.count(), 2)

    def test_list_programmes(self):
        url = reverse('programme-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_programme(self):
        url = reverse('programme-delete', kwargs={'pk': self.programme.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Programme.objects.count(), 0)


class LecturerTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')
        self.programme = Programme.objects.create(name='Test Programme', duration='4 years')
        self.lecturer = Lecturer.objects.create(name='Test Lecturer', lecturer_programme=self.programme)

    def test_create_lecturer(self):
        url = reverse('lecturer-list')
        data = {'name': 'New Lecturer', 'lecturer_programme': self.programme.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lecturer.objects.count(), 2)

    def test_list_lecturers(self):
        url = reverse('lecturer-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_lecturer(self):
        url = reverse('lecturer-delete', kwargs={'pk': self.lecturer.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lecturer.objects.count(), 0)


class MarksTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')
        self.marks = Marks.objects.create(programmeMarks='A')

    def test_create_marks(self):
        url = reverse('marks-list')
        data = {'programmeMarks': 'B'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Marks.objects.count(), 2)

    def test_list_marks(self):
        url = reverse('marks-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_marks(self):
        url = reverse('marks-delete', kwargs={'pk': self.marks.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Marks.objects.count(), 0)


class TuitionFeeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')
        self.programme = Programme.objects.create(name='Test Programme', duration='4 years')
        self.tuition_fee = TuitionFee.objects.create(programme=self.programme, fee='5000')

    def test_create_tuition_fee(self):
        url = reverse('tuitionfee-list')
        data = {'programme': self.programme.id, 'fee': '6000'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TuitionFee.objects.count(), 2)

    def test_list_tuition_fees(self):
        url = reverse('tuitionfee-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_tuition_fee(self):
        url = reverse('tuitionfee-delete', kwargs={'pk': self.tuition_fee.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TuitionFee.objects.count(), 0)


class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'password': 'newpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)