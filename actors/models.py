from django.db import models

class Actor(models.Model):
    ROLE_CHOICES = [
        ('victim', 'Victim'),
        ('suspect', 'Suspect'),
        ('witness', 'Witness'),
        ('detective', 'Detective'),
    ]

    name = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    description = models.TextField()
    testimony = models.TextField(blank=True, null=True)  # Only for victims/suspects
    profile_picture_url = models.URLField()
    is_criminal = models.BooleanField(default=False)  # To track criminal status

    def save(self, *args, **kwargs):
        if self.is_criminal and self.role != 'suspect':
            raise ValueError("Only suspects can be marked as criminals")
        super().save(*args, **kwargs)
