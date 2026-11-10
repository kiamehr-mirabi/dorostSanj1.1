from django.db import models


class session(models.Model):

    sess = models.IntegerField()
    dorost = models.BigIntegerField()
    best_of_dorost = models.IntegerField()
    def __str__(self):
        return f"جلسه {self.sess}"
    
class donator(models.Model):
    name = models.CharField()
    class type_choise(models.TextChoices):
        TOMAN = 'toman', 'تومن'
        CRYPTO = 'crypto', 'crypto'
    type_money = models.CharField(max_length=10,choices=type_choise.choices)
    value = models.BigIntegerField()
    discriptions = models.CharField(null=True)
    def __str__(self):
        return f"نام {self.name}"