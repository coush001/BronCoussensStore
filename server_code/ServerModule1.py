import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import stripe
import anvil.email
import time

@anvil.server.callable
def add_message(name, email, message):
  app_tables.websitecontact.add_row(name=name, email=email, message=message, date=datetime.now())
  anvil.email.send(from_name="BronwenCoussensCeramics: New website contact!",
            to="hbcoussens@gmail.com",
            subject="BronwenCoussensCeramics: New website contact!!",
            text=f"New web contact from {name} ({email})\nMessage: {message}")
  
@anvil.server.callable
def add_subscriber(email):
  app_tables.subscribers.add_row(email=email, date_added=datetime.now())
  anvil.email.send(from_name="BronwenCoussensCeramics: New request for subscription",
          to="hbcoussens@gmail.com",
          subject="BronwenCoussensCeramics: New request for subscription!!",
          text=f"New web sub request:  ({email})\n")
  
@anvil.server.callable
def add_order(charge_id, order, items, shipping, potcost, total, stripe, shipaddress):
  app_tables.orders.add_row(charge_id=charge_id, order=order, date=datetime.now(), shipping=shipping, potcost=potcost, totalcost=total, stripe=stripe, shipaddress=shipaddress)
  for i in items:
    i['product']['available'] = False
  print('Order added with date and item removed from inv')


  anvil.email.send(from_name="BronwenCoussensCeramics: New Order!",
              to="hbcoussens@gmail.com",
              subject="BronwenCoussensCeramics: New Order!",
              text=f"\nItems:\n{order} \n\n Stripe Output:\n {stripe}   ,\n\nShipping address:\n {shipaddress} \n\nTotal Amount:\n  {total}" )
  
