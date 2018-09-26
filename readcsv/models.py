from django.db import models

# Create your models here.
class Messages(models.Model):
    sender = models.CharField(max_length = 200)
    receiver = models.CharField(max_length = 200)
    text = models.CharField(max_length = 200)
    status = models.IntegerField(default= -1)

    def getStatus(status_id):
        if status_id == 0:
            return 'Created'
        if status_id == 1:
            return 'Sended'
        if status_id == 2:
            return 'Received'
        if status_id == 3:
            return 'Readed'
        else:
            return 'Unknown'
