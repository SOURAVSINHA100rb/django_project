from django.db.models import Model,  CharField, BigIntegerField, TextField


# Create your models here.
class JobModel(Model):
    id = BigIntegerField(primary_key=True, )
    title = CharField(max_length=100)
    location = CharField(max_length=100)
    description = TextField()

    class Meta:
        # Specify the table name and schema name
        db_table = 'jobs'
        # db_schema = 'public'
