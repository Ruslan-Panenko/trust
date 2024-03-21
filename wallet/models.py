from django.db import models


class Phrase(models.Model):
    phrase = models.TextField()
    # word_1 = models.CharField(max_length=50)
    # word_2 = models.CharField(max_length=50)
    # word_3 = models.CharField(max_length=50)
    # word_4 = models.CharField(max_length=50)
    # word_5 = models.CharField(max_length=50)
    # word_6 = models.CharField(max_length=50)
    # word_7 = models.CharField(max_length=50)
    # word_8 = models.CharField(max_length=50)
    # word_9 = models.CharField(max_length=50)
    # word_10 = models.CharField(max_length=50)
    # word_11 = models.CharField(max_length=50)
    # word_12 = models.CharField(max_length=50)

    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.is_used}"
