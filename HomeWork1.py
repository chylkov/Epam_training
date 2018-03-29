
# coding: utf-8

# In[12]:

n_student=int(input("Количество студентов: "))
n_task=int(input("Количество заданий на курсе: "))

# Инициализация количества в ТОП
top=3

# контейнер где храним все оценки
statement_list=[]

# список имен
name_list=[]

# сумма оценок по студентам
name_sum_mark =[]

# список предметов
obj_list=list(range(n_task))

# сумма оценок по предметам
obj_sum_mark=[0 for i in range(n_task)]

for name in range(n_student):
    name_list.append(input(f"Фамилия, имя и отчество студента {name + 1}: "))
    rate_list = []
    for task in range(n_task):
        
        m = int(input(f"Оценка за задание {task + 1} студента {name_list[name] }: "))
        while m<0 or m>10:
            print("Неверное значение оценки. Оценка должна быть от 0 до 10")
            m = int(input(f"Оценка за задание {task + 1} студента {name_list[name] }: "))

        rate_list.append(m)
        obj_sum_mark[task]=obj_sum_mark[task] + rate_list[task]
                         
    statement_list.append(rate_list)
    name_sum_mark.append(sum(rate_list))


#делаю копию списков, так как далее из копии будут удалятся элементы
name_list2=list(name_list)
name_sum_mark2=list(name_sum_mark)

print(f'ТОП-{top} студента по рейтингу:')

for i in range(min(top,n_student)):
    print(name_list2[name_sum_mark2.index(max(name_sum_mark2))])
    del name_list2[name_sum_mark2.index(max(name_sum_mark2))]
    del name_sum_mark2[name_sum_mark2.index(max(name_sum_mark2))]
    

obj_list2=list(obj_list)
obj_sum_mark2=list(obj_sum_mark)


print(f'ТОП-{top} самых сложных предметов:')

for i in range(min(top,n_task)):
    print(obj_list2[obj_sum_mark2.index(min(obj_sum_mark2))]+1)
    del obj_list2[obj_sum_mark2.index(min(obj_sum_mark2))]
    del obj_sum_mark2[obj_sum_mark2.index(min(obj_sum_mark2))]


                         


