from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)
    level = models.CharField(max_length=8, choices=(
        ('admin', 'admin'),
        ('user', 'user'),
        ('new', 'new'),
    ))
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user_list'
        verbose_name = 'User'
        verbose_name_plural = 'Users'