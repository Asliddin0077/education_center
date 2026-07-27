from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer


# 1. Barcha studentlarni ko'rish
class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# 2. Bitta studentni ko'rish
class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# 3. Yangi student yaratish
class StudentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# 4. Studentni tahrirlash
class StudentUpdateAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# 5. Studentni o'chirish
class StudentDeleteAPIView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer