
# coding: utf-8

# In[ ]:

def course(data):
    """
    Возвращает список курсов
    :param data: list of dict
    :return: set of course
    """
    return {item['course'] for item in data}


def data_course(data, course):
    """
    Возвращает отфильтрованные данные по оценке по заданному 'course'
    :param data: list of dict
    :param course: str
    :return: list of dict
    """
    return sorted([item for item in data if item['course'] == course], key=lambda x: x['rate'], reverse=True)


def top_course(data, course, top=1):
    """
    Выводит список топ студентов по курсу
    :param data:list of dict
    :param course: str
    :param top: int
    :return: none
    """
    print('\n',course)
    [print(item['name'], item['rate']) for item, stage in
     zip(data_course(data, course), range(1, top+1))]


def top_all_courses(data, top=1):
    """
    Вывод топ студентов по всем курсам
    :param data: list of dict
    :param top: int
    :return: none
    """
    [top_course(data, course) for course in course(data)]


if __name__=='__main__':
    list_student = [{'name': 'Alexey', 'rate': 2, 'course': 'Python'}, 
                {'name': 'Anton', 'rate': 4, 'course': 'Python'}, 
                {'name': 'Nasty', 'rate': 5, 'course': 'English'}, 
                {'name': 'Marina', 'rate': 2, 'course': 'English'}]

    print(top_all_courses(list_student, 'English'))

