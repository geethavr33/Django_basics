from django.db import models
from user.models import User
from mastercodes.models import MasterCode

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    bio = models.TextField(blank=True)
    weight = models.FloatField()
    height = models.FloatField()
    religion = models.ForeignKey(MasterCode, on_delete=models.CASCADE, related_name='profile_religion')

    caste = models.ForeignKey(MasterCode, on_delete=models.CASCADE, related_name='profile_caste')
    education = models.ForeignKey(MasterCode, on_delete=models.CASCADE, related_name='profile_education')
    gender = models.ForeignKey(MasterCode, on_delete=models.CASCADE, related_name='profile_gender')
    income = models.ForeignKey(MasterCode, on_delete=models.CASCADE, related_name='profile_income')
    profession = models.ForeignKey(MasterCode, on_delete=models.CASCADE, related_name='profile_profession')
   
    language = models.CharField(max_length=255)
    address = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='profile_images/')
    marital_status = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default='Active')
    family_details = models.TextField(blank=True)
    date_of_birth = models.DateField()
    deactivate = models.BooleanField(default=False)
def save(self, *args, **kwargs):
    if self.caste and self.religion:
        valid_castes = MasterCode.objects.filter(type='Caste', parent_code=self.religion.code)
        if not valid_castes.filter(code=self.caste.code).exists():
            raise ValueError(f"Caste '{self.caste.display_text}' is not valid for Religion '{self.religion.display_text}'.")
    super().save(*args, **kwargs)

    def __str__(self):
        return f"Profile of {self.user.username}"
