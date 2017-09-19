from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    director = models.ForeignKey(Person, related_name='directed_movie')
    actors = models.ManyToManyField(Person, through='Role')
    year = models.IntegerField()


class Role(models.Model):
    movie = models.ForeignKey(Movie)
    actor = models.ForeignKey(Person, related_name='role')
    description = models.TextField()




