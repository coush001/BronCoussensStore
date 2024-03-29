from ._anvil_designer import ProductTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..AddToCart import AddToCart

class Product(ProductTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if self.item['available']==False:
      self.soldButton.visible = True
      self.add_button.visible = False
      self.added_button.visible = False
    # Any code you write here will run when the form opens.

  def add_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(content=AddToCart(item=self.item),
                         large=True)

  def added_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass





