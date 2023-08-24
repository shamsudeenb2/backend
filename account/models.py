from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=200,)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'date_of_birth']

    # class Meta:
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')

    # def get_full_name(self):
    #     '''
    #     Returns the first_name plus the last_name, with a space in between.
    #     '''
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    # def get_short_name(self):
    #     '''
    #     Returns the short name for the user.
    #     '''
    #     return self.first_name

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     '''
    #     Sends an email to this User.
    #     '''
    #     send_mail(subject, message, from_email, [self.email], **kwargs)
        

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    sickness_name = models.CharField(max_length=1000, blank=False, default="Hiv/Aids")
    gender= models.CharField(max_length=100, blank=False, default="Male")
    profile_img=models.ImageField(upload_to='images/', max_length=255, null=True, blank=True)
    createdAt=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.sickness_name
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()