from django.db import models
from ckeditor.fields import RichTextField

class Code(models.Model):
    input_code = RichTextField(blank=True, null=True)
