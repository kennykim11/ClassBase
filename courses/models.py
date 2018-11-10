from django.db import models

class Course(models.Model):
    name: str = models.TextField(default='Introduction to Django')
    idName: str = models.TextField(default='HELP-123')
    serial: int = models.IntegerField(default=1)
    credits: int = models.IntegerField(default=3)
    """coreqs = models.ForeignKey('self', related_name='coreqs', on_delete=models.DO_NOTHING)
    prereqs = models.ForeignKey('self', related_name='prereqs', on_delete=models.DO_NOTHING)
    sameAs = models.ForeignKey('self', related_name='sameAs', on_delete=models.DO_NOTHING)
    countsAs = models.ForeignKey('self', related_name='countsAs', on_delete=models.DO_NOTHING)"""
    coreqs = models.TextField(default='HELP-123')
    prereqs = models.TextField(default='HELP-123')
    sameAs = models.TextField(default='HELP-123')
    countsAs = models.TextField(default='HELP-123')

    def __str__(self):return self.name

class Section(models.Model):
    serial: str = models.TextField()
    year: int = models.IntegerField(default=2018)
    semester: int = models.IntegerField(default=1)
    status: int = models.IntegerField(default=1) #0=Open, 1=Closed
    currentlyEnrolled: int = models.IntegerField(default=0)
    maxStudents: int = models.IntegerField(default=20)
    cost: float = models.FloatField(default=0.0)

class Room(models.Model):
    number: int = models.IntegerField(default=1000)
    building: str = models.TextField(default='ABC')
    rooms = models.ForeignKey(Section, on_delete=models.CASCADE)

class Day(models.Model):
    day: int = models.IntegerField(default=1)
    time = models.DateTimeField()
    times = models.ForeignKey(Section, on_delete=models.CASCADE)