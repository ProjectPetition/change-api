from peewee import *
import csv

db_config = open("db_config", 'r')

db_config_parser = csv.reader(db_config, delimiter=',')

for entry in db_config_parser:

    password = entry[1]


database = MySQLDatabase('changeDB', **{'passwd': password})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Organizations(BaseModel):
    address = CharField(max_length=50, null=True)
    city = CharField(max_length=50, null=True)
    country_code = CharField(max_length=50, null=True)
    country_name = CharField(max_length=50, null=True)
    location = CharField(max_length=50, null=True)
    mission = TextField(null=True)
    name = CharField(max_length=50, null=True)
    organization = PrimaryKeyField(db_column='organization_id')
    organization_url = CharField(max_length=300, null=True)
    postal_code = CharField(max_length=50, null=True)
    state_province = CharField(max_length=50, null=True)
    website = CharField(max_length=300, null=True)

    class Meta:
        db_table = 'organizations'

class Petitions(BaseModel):
    category = CharField(max_length=50, null=True)
    created_at = DateTimeField(null=True)
    end_at = DateTimeField(null=True)
    goal = IntegerField(null=True)
    image_url = CharField(max_length=300, null=True)
    letter_body = TextField(null=True)
    organization = IntegerField(db_column='organization_id', null=True)
    petition = PrimaryKeyField(db_column='petition_id')
    signature_count = IntegerField(null=True)
    status_petition = CharField(max_length=30, null=True)
    target = IntegerField(db_column='target_id', null=True)
    title = TextField(null=True)
    url = CharField(max_length=300, null=True)
    user = IntegerField(db_column='user_id', null=True)

    class Meta:
        db_table = 'petitions'

class Reasons(BaseModel):
    id = PrimaryKeyField(db_column='ID')
    author_name = CharField(max_length=50, null=True)
    author_url = CharField(max_length=300, null=True)
    content = TextField(null=True)
    created_on = DateTimeField(null=True)
    like_count = IntegerField(null=True)
    petition = IntegerField(db_column='petition_id', null=True)

    class Meta:
        db_table = 'reasons'

class Signatures(BaseModel):
    id = PrimaryKeyField(db_column='ID')
    city = CharField(max_length=50, null=True)
    country = CharField(max_length=50, null=True)
    country_code = CharField(max_length=10, null=True)
    name = CharField(max_length=250, null=True)
    petition = IntegerField(db_column='petition_id', null=True)
    phone = CharField(max_length=10, null=True)
    reason = TextField(null=True)
    signed_on = DateTimeField(null=True)
    state = CharField(max_length=50, null=True)
    user = IntegerField(db_column='user_id', null=True)

    class Meta:
        db_table = 'signatures'

class Target(BaseModel):
    id = PrimaryKeyField(db_column='ID')
    petition = IntegerField(db_column='petition_id', null=False)
    name = CharField(max_length=50, null=True)
    target_area = CharField(max_length=50, null=True)
    title = TextField(null=True)
    type = CharField(max_length=50, null=True)

    class Meta:
        db_table = 'target'

class TargetPetition(BaseModel):
    id = PrimaryKeyField(db_column='ID')
    petition = IntegerField(db_column='petition_id', null=True)
    target = IntegerField(db_column='target_id', null=True)

    class Meta:
        db_table = 'target_petition'

class Updates(BaseModel):
    id = PrimaryKeyField(db_column='ID')
    author_name = CharField(max_length=50, null=True)
    author_url = CharField(max_length=300, null=True)
    content = TextField(null=True)
    created_on = DateTimeField(null=True)
    petition = IntegerField(db_column='petition_id', null=True)

    class Meta:
        db_table = 'updates'

class Users(BaseModel):
    city = CharField(max_length=50, null=True)
    country_code = CharField(max_length=10, null=True)
    country_name = CharField(max_length=50, null=True)
    location = CharField(max_length=50, null=True)
    name = CharField(max_length=50, null=True)
    state_province = CharField(max_length=50, null=True)
    user = PrimaryKeyField(db_column='user_id')
    user_url = CharField(max_length=300, null=True)

    class Meta:
        db_table = 'users'

