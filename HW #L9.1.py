
# coding: utf-8

# In[ ]:

import datetime as dt
import traceback as tr
import time


class redirect:
    """
    Контексный менеджер, который выводит ионфмарцию о случившихся ошибках, дате, времени выполенния кода
    """
    def __init__(self, name_file="log.txt"):
        """
        :param name_file: название файла
        """
        self._name_file = name_file

    def __enter__(self):
        self._date_start = dt.datetime.today()
        self._t1 = time.time()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_value:
            with open(self._name_file, 'w') as fout:
                print(f"Дата начала: {self._date_start},\nДата окончания: {dt.datetime.today()}", file=fout)
                self._t2 = time.time()
                t3 = self._t2 - self._t1
                print("Время выполнения: %.02f sec" % (t3), file=fout)
                print(f"Ошибка: {exception_value}", file=fout)
                print("Traceback: ", file=fout)
                tr.print_tb(traceback, file=fout)

if __name__=='__main__':
    with redirect("log.txt"):
        time.sleep(3)
        2/0

