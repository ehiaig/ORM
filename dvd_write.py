from dvdrentalmodels import Payment, Rental, Inventory, Customer, Film
from peewee import *

# my_db = PostgresqlDatabase('dvdrental',
#                            host = 'localhost',
#                            user = 'postgres',
#                            password = '$Make2016$',
#                            port = '5432')

if __name__=='__main__':

    Q = Rental.select(Rental, Customer, Inventory, Film). \
        join(Customer, on=(Customer.customer == Rental.customer)). \
        join(Inventory, on=(Inventory.inventory == Rental.inventory)). \
        join(Film, on=(Film.film == Inventory.film)). \
        order_by(Rental.rental_date.desc()).limit(10)

    for u in Q:
        # print(u._data['rental_date']) #This prints the result as object
        # print(u.__dict__)#This prints the result as dictionary
        print(" Name: {}\n Movie Title:{}\n Return Date:{}".format(u.customer.first_name+' '+u.customer.last_name, u.inventory.film.title, u._data['rental_date']))
        print(' ')
