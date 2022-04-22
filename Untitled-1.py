class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = float()

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_count = 0
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average = sum(map(sum, self.grades.values())) / grades_count
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(self.average, 1)}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average < other.average
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average = float()

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average = sum(map(sum, self.grades.values())) / grades_count
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.average, 1)}"
 
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average < other.average

class Reviewer(Mentor):

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
        
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def calculating_average_lecturer(lecturer_list, course_name):

    sum = 0
    count_all_lecturer = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum += lect.average
            count_all_lecturer += 1
    average_for_all = sum / count_all_lecturer
    return round(average_for_all, 1)

def calculating_average_students(students_list, course_name):

    sum = 0
    count_all_students = 0
    for student in students_list:
        if student.courses_in_progress == [course_name]:
            sum += student.average
            count_all_students += 1
    average_for_all = sum / count_all_students
    return round(average_for_all, 1)

# Создаем лекторов и закрепляем за курсом
lecturer_1 = Lecturer('Ivan', 'Ivanov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Petr', 'Petrov')
lecturer_2.courses_attached += ['Java']

# создаем проверяющих и закрепляем за курсом
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Ostap', 'Bender')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

# создаем студентов и определяем курсы
student_1 = Student('Anton', 'Naumov', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Maxim', 'Naumov', 'your_gender')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

# выстявляем оценки лекторам за лекции
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Python', 7)

student_2.rate_hw(lecturer_2, 'Java', 5)
student_2.rate_hw(lecturer_2, 'Java', 7)
student_2.rate_hw(lecturer_2, 'Java', 8)

student_2.rate_hw(lecturer_2, 'Java', 5)
student_2.rate_hw(lecturer_2, 'Java', 8)
student_2.rate_hw(lecturer_2, 'Java', 9)

# выставляем оценки студентам за домашнее задание
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 5)

reviewer_2.rate_hw(student_1, 'Python', 6)
reviewer_2.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_1, 'Python', 8)

# выставляем оценки студентам за домашнее задание
reviewer_1.rate_hw(student_2, 'Java', 6)
reviewer_1.rate_hw(student_2, 'Java', 8)
reviewer_1.rate_hw(student_2, 'Java', 9)

reviewer_2.rate_hw(student_2, 'Java', 4)
reviewer_2.rate_hw(student_2, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Java', 9)

# Выводим лекторов
print(f'Список лекторов:\n\n{lecturer_1}\n\n{lecturer_2}')
print()

# Выводим результат сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer_1.name} {lecturer_1.surname} > {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}')
print()
# Выводим студентов
print(f'Список студентов:\n\n{student_1}\n\n{student_2}')
print()
print(f'Результат сравнения студентов (по средним оценкам за домашние задания): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 < student_2}')
print()

# создание списка студентов
student_list = [student_1, student_2]

# создание списка лекторов
lecturer_list = [lecturer_1, lecturer_2]

print(f"Средняя оценка всех лекторов по курсу {'Python'}: {calculating_average_lecturer(lecturer_list, 'Python')}")
print()

print(f"Средняя оценка за домашние задания всех студентов по курсу {'Java'}: {calculating_average_students(student_list, 'Java')}")
print()
