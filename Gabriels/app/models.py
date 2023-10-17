from django.db import models

# Create your models here.
#### we are used already existing table so we provide pymysql module
#### (--pip install mysql --)

"""~~~ settings.py"""
### import pymysql
### pymysql.install_as_MYSQLdb()
"""~~~~X~~~~"""

###In Terminal
## > py manage.py inspectdb
## then load all tables in that database
## we can copy and paste in models.py
## now we can access table

class Details(models.Model): ### Details table is in the gabriels database
    userid = models.AutoField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=100, blank=True, null=True)  # Field name made lowercase.    useraddress = models.CharField(db_column='UserAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userphone = models.CharField(db_column='UserPhone', unique=True, max_length=25, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    usermail = models.CharField(db_column='UserMail', unique=True, max_length=30, blank=True, null=True)  # Field name made lowercase.
    userprofileimg = models.TextField(db_column='UserProfileImg', blank=True, null=True)  # Field name made lowercase.    
    dateupdated = models.DateTimeField(db_column='DateUpdated', blank=True, null=True)  # Field name made lowercase.      

    class Meta:
        managed = False
        db_table = 'details'

