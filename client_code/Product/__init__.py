from ._anvil_designer import ProductTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..expandedItem import expandedItem

class Product(ProductTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if self.item['available'] is False:
      self.soldButton.visible = True
      self.add_button.visible = False
      self.added_button.visible = False
    # Any code you write here will run when the form opens.

  def add_(self, **event_args):
    self.added_button.visible = True
    self.remove_button.visible = True
    self.add_button.visible = False
    pass

  def remove_(self, **event_args):
    self.added_button.visible = False
    self.remove_button.visible = False
    self.add_button.visible = True
    pass

  def view_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(content=expandedItem(product=self, item=self.item), large=True)

  def add_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().add_to_cart(self.item)
    self.add_()
  
  def remove_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().remove_from_cart(self.item)
    self.remove_()
    pass





