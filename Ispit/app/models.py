from django.contrib.auth.models import User
from django.db import models


# Автори може да бидат додадени само од супер-корисници
# Книги можат да бидат додадени само од автори и авторот по автоматизам се додава како автор на книгата
# Супер-корисници може да пребаруваат книги според зборови во опис
# (za has change da moze da raboti, mora da ima user vo Book)
# Книги можат да бидат менувани само од нивите автори
# Авторите може да ги листаат сите книги за кои имаат опис
# (se stava text field pole i od nego se zemaat vrednostite, NE se pravi exclude na ova pole)
# Авторите на книгите се додаваат преку запирка

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    author_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
