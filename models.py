from django.db import models


class President(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    slogan = models.TextField()


class Position(models.Model):
    position_name = models.CharField(max_length=255)

    def __str__(self):
        return self.position_name


class Choice(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.position
        return self.choice_text
