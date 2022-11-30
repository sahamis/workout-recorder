from django.conf import settings
from django.db import models
from django.utils import timezone

class Record(models.Model):
    kind_of_workout=models.CharField(max_length=30)
    equipment_type=models.CharField(max_length=10)
    
    workout_weight1=models.FloatField()
    workout_rep1=models.SmallIntegerField()
    workout_weight2=models.FloatField(blank=True,null=True)
    workout_rep2=models.SmallIntegerField(blank=True,null=True)
    workout_weight3=models.FloatField(blank=True,null=True)
    workout_rep3=models.SmallIntegerField(blank=True,null=True)
    workout_weight4=models.FloatField(blank=True,null=True)
    workout_rep4=models.SmallIntegerField(blank=True,null=True)
    workout_weight5=models.FloatField(blank=True,null=True)
    workout_rep5=models.SmallIntegerField(blank=True,null=True)
    workout_weight6=models.FloatField(blank=True,null=True)
    workout_rep6=models.SmallIntegerField(blank=True,null=True)
    workout_weight7=models.FloatField(blank=True,null=True)
    workout_rep7=models.SmallIntegerField(blank=True,null=True)
    workout_weight8=models.FloatField(blank=True,null=True)
    workout_rep8=models.SmallIntegerField(blank=True,null=True)
    workout_weight9=models.FloatField(blank=True,null=True)
    workout_rep9=models.SmallIntegerField(blank=True,null=True)
    workout_weight10=models.FloatField(blank=True,null=True)
    workout_rep10=models.SmallIntegerField(blank=True,null=True)
    
    workout_date=models.DateField(default=timezone.now)
    free_comment=models.TextField(blank=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
