from django.db import models

# Create your models here.

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

    @classmethod
    def create_demo_user(cls):
        demo_user = cls(username="demo-user")
        demo_user.set_password("demo-password")
        demo_user.save()
        return demo_user


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    task = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
