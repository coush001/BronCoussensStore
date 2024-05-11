from ._anvil_designer import expandedItemTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class expandedItem(expandedItemTemplate):
  def __init__(self, product, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.product = product
    self.added_button.visible = self.product.added_button.visible

  def add_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().add_to_cart(self.item)
    self.product.add_()
    self.add_button.visible = False
    self.added_button.visible = True
    self.remove_button.visible = True

  def remove_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().remove_from_cart(self.item)
    self.product.remove_()
    self.add_button.visible = True
    self.added_button.visible = True
    self.remove_button.visible = False
    pass

