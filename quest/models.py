from django.db import models

class Question(models.Model):
	'''
		Model class reprsenting a Question
	'''
	statement = models.CharField("Statement",max_length = 5000)
	ans = models.CharField("Answer",max_length  = 100)
	weight = models.IntegerField("Weight")
	success = models.IntegerField("Success") # how many users have solved it
	

