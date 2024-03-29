from ._anvil_designer import MainTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..OnlineGallery import OnlineGallery
from ..Contact import Contact
from ..About import About
from ..Cart import Cart
from ..Blog import Blog


class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.navigate(self.home_link, Home())
    self.cart_items = []
    
    for link in [self.home_link, self.shop_link, self.about_link, self.contact_link, self.insta_link, self.cart_link]:
      link.role = ['spaced-title', 'display-none-responsive']
    
  def add_to_cart(self, product):
    #if item is already in cart, just update the quantity
    self.cart_items.append({'product': product})
    print(self.cart_items)
    
  def navigate(self, active_link, form):
    for i in [self.home_link, self.shop_link, self.about_link, self.contact_link, self.cart_link, self.blog_link]:
      i.foreground = 'theme:Primary 700'
      i.background = 'theme:Secondary 500'
    active_link.background = 'theme:White'
    active_link.foreground = 'theme:RichBlue'
    self.column_panel_1.clear()
    self.column_panel_1.add_component(form, full_width_row=True)

  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.home_link, Home())

  def shop_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.shop_link, OnlineGallery())

  def blog_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.blog_link, Blog())

  def about_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.about_link, About())
    
  def contact_link_click(self, **event_args):
    """This method is called when the Link is shown on the screen"""
    self.navigate(self.contact_link, Contact())

  def cart_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.cart_link, Cart(items=self.cart_items))

  def subscribe_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    email = self.subscribe_textbox.text
    if email:
      anvil.server.call('add_subscriber', email)
      self.subscribe_textbox.text = None
      Notification("Thanks for subscribing!").show()

 









