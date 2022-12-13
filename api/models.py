from django.db import models
''' Here is where we create our Database replica,
    how we wnat our DB tables to look like.
    Every class will represent a table in the DB
    and will inherit from the Model Class
    attributes will represent columns
'''
class Note(models.Model):
    body =  models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[0:50]
