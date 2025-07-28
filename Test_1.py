from abc import ABC, abstractmethod
class Formatted(ABC): #создаем абстрактный клас
    @abstractmethod
    def format(self):
        pass
class TextFormatted(Formatted):
    def format(self):
        print(report.tittle)
        print(report.content)

class HtmlFormatted(Formatted):
    def format(self):
        print(f"<h1>{report.tittle}</h1>")
        print(f"<p>{report.content}</p>")

class Report:
    def __init__(self, tittle, content, formatted):
        self.tittle = tittle
        self.content = content
        self.formatted = formatted #в formatted сохраняется объект класса либо HtmlFormatted либо TextFormatted

    def docPrinter(self):
        self.formatted.format() #вызываем функцию format  у характеристика formated

report  = Report("Заголовок отчета", "это текст отчета его тут много", HtmlFormatted())
report.docPrinter()