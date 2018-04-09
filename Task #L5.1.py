
# coding: utf-8

# In[ ]:

# Task 1
from datetime import datetime

class Wine:
    
    def __init__(self, name, trade_mark, country, bottling_date, note):
        """
        Инициализация вина. В качестве атрибутов выступают следуюшие:
        name - назвае вина
        trade_mark - торговая марка
        country - страна
        bottling_date - дата розлива в формате "DD/MM/YY"
        note - примечание
        """
        
        
        
        self.name = name
        self.trade_mark = trade_mark
        self.country = country
        self.bottling_date = datetime.strptime(bottling_date, "%d/%m/%y")
        self.note = note
        
    def info(self):
        """
        Вывод информации по конкретному вину:
        name - назвае вина
        trade_mark - торговая марка
        country - страна
        bottling_date - дата розлива в формате "DD/MM/YY"
        note - примечание
        """
        

        return(self.name,self.trade_mark,self.country, 
               datetime.strftime(self.bottling_date, "%d/%m/%y"),  self.note)
    
    
    def exposure(self):
        """
        Расчет выдержки вина в годах (расчет выдержки на текущую дату)
        """

        today = datetime.today()
        return (today.year - self.bottling_date.year -
                ((today.month, today.day) < (self.bottling_date.month, self.bottling_date.day)))

