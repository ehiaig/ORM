from peewee import *
from playhouse.postgres_ext import *

# database = PostgresqlDatabase('dvdrental', **{})
#
class UnknownField(object):
    def __init__(self, *_, **__): pass

database = PostgresqlDatabase('dvdrental',
                           host = 'localhost',
                           user = 'postgres',
                           password = '$Make2016$',
                           port = '5432')
class BaseModel(Model):
    class Meta:
        database = database

class Actor(BaseModel):
    actor = PrimaryKeyField(db_column='actor_id')
    first_name = CharField()
    last_name = CharField(index=True)
    last_update = DateTimeField()

    class Meta:
        db_table = 'actor'

class Country(BaseModel):
    country = CharField()
    country_id = PrimaryKeyField()
    last_update = DateTimeField()

    class Meta:
        db_table = 'country'

class City(BaseModel):
    city = CharField()
    city_id = PrimaryKeyField()
    country = ForeignKeyField(db_column='country_id', rel_model=Country, to_field='country_id')
    last_update = DateTimeField()

    class Meta:
        db_table = 'city'

class Address(BaseModel):
    address = CharField()
    address2 = CharField(null=True)
    address_id = PrimaryKeyField()
    city = ForeignKeyField(db_column='city_id', rel_model=City, to_field='city_id')
    district = CharField()
    last_update = DateTimeField()
    phone = CharField()
    postal_code = CharField(null=True)

    class Meta:
        db_table = 'address'

class Category(BaseModel):
    category = PrimaryKeyField(db_column='category_id')
    last_update = DateTimeField()
    name = CharField()

    class Meta:
        db_table = 'category'

class Customer(BaseModel):
    active = IntegerField(null=True)
    activebool = BooleanField()
    address = ForeignKeyField(db_column='address_id', rel_model=Address, to_field='address_id')
    create_date = DateField()
    customer = PrimaryKeyField(db_column='customer_id')
    email = CharField(null=True)
    first_name = CharField()
    last_name = CharField(index=True)
    last_update = DateTimeField(null=True)
    store = IntegerField(db_column='store_id', index=True)

    class Meta:
        db_table = 'customer'

class Language(BaseModel):
    language = PrimaryKeyField(db_column='language_id')
    last_update = DateTimeField()
    name = CharField()

    class Meta:
        db_table = 'language'

class Film(BaseModel):
    description = TextField(null=True)
    film = PrimaryKeyField(db_column='film_id')
    fulltext = TSVectorField(index=True)
    language = ForeignKeyField(db_column='language_id', rel_model=Language, to_field='language')
    last_update = DateTimeField()
    length = IntegerField(null=True)
    rating = UnknownField(null=True)  # USER-DEFINED
    release_year = IntegerField(null=True)
    rental_duration = IntegerField()
    rental_rate = DecimalField()
    replacement_cost = DecimalField()
    special_features = UnknownField(null=True)  # ARRAY
    title = CharField(index=True)

    class Meta:
        db_table = 'film'

class FilmActor(BaseModel):
    actor = ForeignKeyField(db_column='actor_id', rel_model=Actor, to_field='actor')
    film = ForeignKeyField(db_column='film_id', rel_model=Film, to_field='film')
    last_update = DateTimeField()

    class Meta:
        db_table = 'film_actor'
        indexes = (
            (('actor', 'film'), True),
        )
        primary_key = CompositeKey('actor', 'film')

class FilmCategory(BaseModel):
    category = ForeignKeyField(db_column='category_id', rel_model=Category, to_field='category')
    film = ForeignKeyField(db_column='film_id', rel_model=Film, to_field='film')
    last_update = DateTimeField()

    class Meta:
        db_table = 'film_category'
        indexes = (
            (('film', 'category'), True),
        )
        primary_key = CompositeKey('category', 'film')

class Inventory(BaseModel):
    film = ForeignKeyField(db_column='film_id', rel_model=Film, to_field='film')
    inventory = PrimaryKeyField(db_column='inventory_id')
    last_update = DateTimeField()
    store = IntegerField(db_column='store_id')

    class Meta:
        db_table = 'inventory'
        indexes = (
            (('film', 'store'), False),
        )

class Staff(BaseModel):
    active = BooleanField()
    address = ForeignKeyField(db_column='address_id', rel_model=Address, to_field='address_id')
    email = CharField(null=True)
    first_name = CharField()
    last_name = CharField()
    last_update = DateTimeField()
    password = CharField(null=True)
    picture = BlobField(null=True)
    staff = PrimaryKeyField(db_column='staff_id')
    store = IntegerField(db_column='store_id')
    username = CharField()

    class Meta:
        db_table = 'staff'

class Rental(BaseModel):
    customer = ForeignKeyField(db_column='customer_id', rel_model=Customer, to_field='customer')
    inventory = ForeignKeyField(db_column='inventory_id', rel_model=Inventory, to_field='inventory')
    last_update = DateTimeField()
    rental_date = DateTimeField()
    rental = PrimaryKeyField(db_column='rental_id')
    return_date = DateTimeField(null=True)
    staff = ForeignKeyField(db_column='staff_id', rel_model=Staff, to_field='staff')

    class Meta:
        db_table = 'rental'
        indexes = (
            (('rental_date', 'inventory', 'customer'), True),
        )

class Payment(BaseModel):
    amount = DecimalField()
    customer = ForeignKeyField(db_column='customer_id', rel_model=Customer, to_field='customer')
    payment_date = DateTimeField()
    payment = PrimaryKeyField(db_column='payment_id')
    rental = ForeignKeyField(db_column='rental_id', rel_model=Rental, to_field='rental')
    staff = ForeignKeyField(db_column='staff_id', rel_model=Staff, to_field='staff')

    class Meta:
        db_table = 'payment'

class RentalNew(BaseModel):
    movie_name = CharField()
    rental_date = DateField()
    renter_name = CharField()
    return_date = DateField()

    class Meta:
        db_table = 'rental_new'

class Store(BaseModel):
    address = ForeignKeyField(db_column='address_id', rel_model=Address, to_field='address_id')
    last_update = DateTimeField()
    manager_staff = ForeignKeyField(db_column='manager_staff_id', rel_model=Staff, to_field='staff', unique=True)
    store = PrimaryKeyField(db_column='store_id')

    class Meta:
        db_table = 'store'

