from django.db import models

class Quiz(models.Model):
	'''
		Quiz class representing a quiz
	'''
	name = models.CharField("Name",max_length = 100,blank=False)
	# start timing of the quiz
	start_date = models.DateField(_(u"Conversation Date"), auto_now_add=True, blank=False)
    start_time = models.TimeField(_(u"Conversation Time"), auto_now_add=True, blank=False)
    # end timing of the quiz
    end_date = models.DateField(_(u"Conversation Date"), auto_now_add=True, blank=False)
    end_time = models.TimeField(_(u"Conversation Time"), auto_now_add=True, blank=False)

class Qbank(models.Model):
	'''
		Model class reprsenting a Question
	'''
	statement = models.CharField("Statement",max_length = 5000)
	ans = models.CharField("Answer",max_length  = 100)
	weight = models.IntegerField("Weight")
	success = models.IntegerField("Success") # how many users have solved it
	quiz_id = models.ForeignKey(Quiz)
