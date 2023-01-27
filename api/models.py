from django.db import models

# Create your models here.
class Note(models.Model):
	# Allow unlimited len of char
	body = models.TextField()

	# For date time track "auto_now" stands for that we will not change the field it will be set automatically
	updated = models.DateTimeField(auto_now=True)

	# Similar to updated but we only want the time stamp of first time when created thus we have used "auto_now_add"
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.body[:50]

	class Meta:
		# Will order query as per last updated will shown first
		ordering = ['-updated']
