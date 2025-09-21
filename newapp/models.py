from django.db import models
import uuid
# Create your models here.

class ghd_pipe_inspection(models.Model):
    objectid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sampler = models.CharField(max_length=50)
    sample_date = models.DateTimeField(auto_now_add=True)
    inspector = models.CharField(max_length=50)

    class LeakLocation(models.TextChoices):
        yes = 'YES', 'Yes'
        no = 'NO', 'No'

    leak_location = models.CharField(max_length=3, choices=LeakLocation.choices)
    time_notified_tva = models.DateField()
    wts_shutdown_time = models.DateField()
    action_taken = models.CharField(max_length=255)
    data_image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.sampler} - {self.sample_date.strftime('%Y-%m-%d %H:%M')}"

