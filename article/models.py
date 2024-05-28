from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    

class Jurnal(models.Model):
    student = models.CharField(max_length=51)
    baho = models.IntegerField()
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.baho}"
    

class Band(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return self.name


MEMBER_CHOICES = (
            ('g', 'Guiter'),
            ('b', 'Bass'),
            ('p', 'Pioner'),
            ('d', 'Dump'),
        )


class Member(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    instrument = models.CharField(
        choices = MEMBER_CHOICES,
        max_length=1,
    )

    band = models.ForeignKey(Band, on_delete = models.CASCADE)


    def __str__(self):
        return self.name
    