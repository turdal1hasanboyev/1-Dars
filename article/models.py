from django.db import models


class User(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    surname = models.CharField(max_length=225, null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    

class Jurnal(models.Model):
    student = models.CharField(max_length=225, null=True, blank=True)
    baho = models.IntegerField(default=0, null=True, blank=True)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.baho}"
    

class Band(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name


MEMBER_CHOICES = (
            ('g', 'Guiter'),
            ('b', 'Bass'),
            ('p', 'Pioner'),
            ('d', 'Dump'),
        )


class Member(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    instrument = models.CharField(
        choices = MEMBER_CHOICES,
        max_length=225,
        null=True, blank=True,
    )
    band = models.ForeignKey(Band, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    