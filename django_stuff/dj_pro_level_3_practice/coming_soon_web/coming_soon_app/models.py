from django.db import models

    
class EarlyUsers(models.Model):
    
    '''
    Defining all the attributes.
    '''
    
    first_name =  models.CharField(max_length=164)
    last_name = models.CharField(max_length=164)
    email = models.CharField(max_length=264, unique=True)

