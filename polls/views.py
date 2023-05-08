from django.shortcuts import render
from faker import Faker

from polls.models import Student, Students


def student(request):
    if request.method == 'GET':
        fake = Faker()
        first_name = str(fake.name()).split(' ')[0]
        last_name = str(fake.name()).split(' ')[1]
        age = fake.random_int(min=20, max=50)
        Student.objects.create(first_name=first_name, last_name=last_name, age=age)
        student = Student.objects.all()
        return render(request, 'new_student.html', {"student": student})


def students(request):
    if request.method == 'GET':
        count = request.GET.get("count", 0)
        print(count)
        if 0 < int(count) <= 100:
            for _ in range(int(count)):
                fake = Faker()
                Students.objects.create(first_name=str(fake.name()).split(' ')[0],
                                        last_name=str(fake.name()).split(' ')[1], age=fake.random_int(min=20, max=50))
            students = Students.objects.all()
            return render(request, 'generate_students.html', {"students": students})
