from django.db.models import Model,  CharField, TextField, AutoField


# Create your models here.
class JobModel(Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=100)
    location = CharField(max_length=100)
    description = TextField()

    class Meta:
        # Specify the table name and schema name
        db_table = 'jobs'
        # db_schema = 'public'
