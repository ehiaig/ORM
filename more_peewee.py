"""
Use peewee to get the last 15 customers who have paid less than $5.50 for a rental and the movie they rented
"""

from dvdrentalmodels import *

if __name__ == '__main__':
    # query = Payment.select(Customer, Inventory, Film, Rental, Payment)\
    #     .join(Rental, on=(Payment.rental == Rental.rental)) \
    #     .join(Customer, on=(Customer.customer == Rental.customer)) \
    #     .join(Inventory, on=(Rental.inventory == Inventory.inventory)) \
    #     .join(Film, on=(Inventory.film == Film.film)) \
    #     .order_by(Payment.payment_date.desc()).\
    #     where(Payment.amount < 5.50).limit(15)
    #
    # for u in query:
    #     print(" Name: {}\n Movie Title:{}\n Amount:{}".format(u.customer.first_name+' '+u.customer.last_name, u.rental.inventory.film.title, u.amount))
    #     print(' ')

    """Find the customers who has taken out the most movies:
A: by number of movies they taken
B: By amount
"""
    # query2a = Rental.select(Customer.customer, Customer.first_name, Customer.last_name,
    #                         fn.COUNT(Customer.customer).alias("no_of_customers")) \
    #     .join(Customer, on=(Rental.customer == Customer.customer)) \
    #     .group_by(Customer.customer) \
    #     .order_by(SQL("no_of_customers").desc()).limit(1).naive()
    #
    # for u in query2a:
    #     print(" Customer Name:{}\n Number of Rentals: {}".format(u.customer.first_name + ' ' + u.customer.last_name,
    #                                                              u.no_of_customers))
    #     print(' ')
    #
    # query2b = Rental.select(Customer.first_name, Customer.last_name, fn.SUM(Payment.amount).alias("total_amount")) \
    #     .join(Customer, on=(Rental.customer == Customer.customer)) \
    #     .join(Payment, on=(Payment.customer == Customer.customer)) \
    #     .group_by(Customer.customer) \
    #     .order_by(SQL("total_amount").desc()).limit(1).naive()

    query2b = Rental.select(Customer, Rental, Payment) \
        .join(Customer, on=(Rental.customer == Customer.customer)) \
        .join(Payment, on=(Payment.customer == Customer.customer)) \
        .group_by(Customer.customer) \
        .order_by(fn.SUM(Payment.amount).desc()).limit(1).naive()

    for u in query2b:
        print(" Customer Name:{}\n Number of Rentals: {}".format(u.customer.first_name + ' ' + u.customer.last_name,
                                                                 fn.SUM(u.amount)))
        print(' ')