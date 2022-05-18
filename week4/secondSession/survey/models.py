from django.db import models

# Create your models here.

class Survey(models.Model) :
    surveyIdx = models.AutoField(primary_key=True)

    # 설문 문항
    question = models.TextField()

    # 선택지 1 ~ 4
    ans1 = models.TextField(null=True)
    ans2 = models.TextField(null=True)
    ans3 = models.TextField(null=True)
    ans4 = models.TextField(null=True)

    def __str__(self) :
        return self.question

class Answer(models.Model) :
    answerIdx = models.AutoField(primary_key=True)
    # surveyIdx = models.ForeignKey(Survey, on_delete=models.CASCADE)
    surveyIdx = models.IntegerField()
    choice = models.TextField()


