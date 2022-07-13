from django.db import models


class Name(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False)
    name = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ability(models.Model):
    id_name = models.ForeignKey(Name, on_delete=models.CASCADE, auto_created=False)
    ability = models.CharField(max_length=200)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.ability