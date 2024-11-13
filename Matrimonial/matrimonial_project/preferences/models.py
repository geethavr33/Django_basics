from django.db import models
from user.models import User
from mastercodes.models import MasterCode

class Preferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=50)
    caste = models.ForeignKey(MasterCode, on_delete=models.CASCADE, related_name='preferences_caste')
    education = models.ForeignKey(MasterCode, on_delete=models.CASCADE, related_name='preferences_education')
    gender = models.ForeignKey(MasterCode, on_delete=models.CASCADE, related_name='preferences_gender')
    income = models.ForeignKey(MasterCode, on_delete=models.CASCADE, related_name='preferences_income')
    profession = models.ForeignKey(MasterCode, on_delete=models.CASCADE, related_name='preferences_profession')
    religion = models.ForeignKey(MasterCode, on_delete=models.CASCADE, related_name='preferences_religion')
    location = models.CharField(max_length=255)
    height = models.FloatField()
    weight = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


def save(self, *args, **kwargs):
    if self.caste and self.religion:
        valid_castes = MasterCode.objects.filter(type='Caste', parent_code=self.religion.code)
        if not valid_castes.filter(code=self.caste.code).exists():
            raise ValueError(f"Caste '{self.caste.display_text}' is not valid for Religion '{self.religion.display_text}'.")
    super().save(*args, **kwargs)


    def __str__(self):
        return f"Preferences of {self.user.username}"
