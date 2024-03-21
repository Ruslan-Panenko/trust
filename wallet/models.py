from django.db import models


class Phrase(models.Model):
    phrase = models.TextField()

    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.is_used}"
