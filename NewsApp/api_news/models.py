from django.db import models

# Create your models here.

class Account(models.Model):
    """
    Storing all users with unique id
    """
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password =models.CharField(max_length=255)

def get_account():
    return Account.objects.get(id=1).id

class History(models.Model):
    """
    storing searched data as history along with user data.
    """
    id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    user = models.ForeignKey(Account, default=get_account, on_delete=models.CASCADE)


