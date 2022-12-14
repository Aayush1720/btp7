from django.db import models

# Create your models here.
class imageModel(models.Model):
    image = models.URLField(max_length=200)
    tag = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['image', 'tag'], name='unique_image_tag_combination'
            )
        ]