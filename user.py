from peewee import PostgresqlDatabase, Model, CharField, BooleanField, IntegerField

psql_db = PostgresqlDatabase("class_orm_db",
                            host = "localhost",
                            user = "postgres",
                            password = "$Make2016$",
                            port = "5432")
class MyUser(Model):
    class Meta:
        database = psql_db

    age = IntegerField(4)
    username = CharField(20)
    password = CharField(10)
    email = CharField(30)

    is_beautiful = BooleanField(default = False)

if __name__ == "__main__":
    MyUser.create_table(fail_silently = True)

    user1 = MyUser(username = 'Precious',
                      password = 'pressy2017',
                      email = 'precious@meltwater.org',
                      age = '20')
    user2 = MyUser(username = 'abu.okari',
                      password = 'sasa',
                      email = 'okari@meltwater.org',
                      age = '35')
    user1.save()
    user2.save()
    user2.delete_instance()
    

    # """To print all users in the database"""
    # for my_user in MyUser.select():
    #     print("email {0} at {1}".format(my_user.username, my_user.email))

    """To print all users whose age is > 20"""
    for my_user in MyUser.select():
        if my_user.age > 20:
            print("email {0} at {1}".format(my_user.username, my_user.email))

    # is_simeon = MyUser.select().where(MyUser.username == 'Simeon')
    #
    # is_not_simeon = MyUser.select().where(MyUser.username != 'Simeon')
    #
    # not_a_child = MyUser.select().where(MyUser.age>21)
    #
    # really_not_a_child = MyUser.select().where(MyUser.age() >21 & (MyUser.username != 'Simeon'))


    # Get the first 10 ugly users
    ugly_ten = MyUser.select().limit(10)

    # Last 5 alphabetically ugly
    alphabetical_ugly = MyUser.select().order_by(MyUser.username).desc().limit(5)

    
