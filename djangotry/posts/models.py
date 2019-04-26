from django.db import models

# Create your models here.
# MVC = MODEL VIEW CONTROLLER


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)




    #for python 2 we need to write __unicode___
    def __unicode__(self):
        return self.title


    #for python 3 we need to write __str__
    def __str__(self):
        return self.title


    # def __str__(self):
    #     return self.content

