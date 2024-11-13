from django.db import models

class MasterCode(models.Model):
    type = models.CharField(max_length=50)
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    display_text = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    parent_code = models.ForeignKey(
    'self', 
    on_delete=models.CASCADE, 
    null=True, 
    blank=True, 
    related_name='children'
)
   

    def __str__(self):
        return f"{self.type}: {self.display_text} ({self.code})"
