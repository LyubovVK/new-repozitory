#Базовые структуры данных.
#Задание "Средний балл":

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_student=sorted(students)
spisok_ = list(sort_student)
print(sort_student)
print()
print(spisok_)
len_=len(spisok_)
print('Средний балл каждого из',len_,'студентов:')
for i in range(0,len_):
    print(sort_student[i], sum(grades[i])/len(grades[i]))

print()
max_ball=0.0
min_ball=5.0
for i in range(0, len_):
    ball_ = sum(grades[i]) / len(grades[i])
    if ball_ > max_ball:
        max_ball=ball_
        i_max=i
    if  min_ball > ball_:
        min_ball=sum(grades[i]) / len(grades[i])
        i_min=i

print('Лучший балл у студента:')
print(sort_student[i_max], max_ball)
print('Худший балл у студента:')
print(sort_student[i_min], min_ball)
