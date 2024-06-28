grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students) # Сортировка по алфавиту.
grades[0] = sum(grades[0])/len(grades[0]) # Вычисление средней оценки. Функция sum() возвращает сумму всех элементов списка, а функция len() возвращает количество элементов в списке.
grades[1] = sum(grades[1])/len(grades[1])
grades[2] = sum(grades[2])/len(grades[2])
grades[3] = sum(grades[3])/len(grades[3])
grades[4] = sum(grades[4])/len(grades[4])

student_performance = {'Aaron': grades[0], 'Bilbo': grades[1], 'Johnny': grades[2], 'Khendrik': grades[3], 'Steve': grades[4]}
print(student_performance)