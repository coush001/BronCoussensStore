from ._anvil_designer import AddToCartTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AddToCart(AddToCartTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def add_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().add_to_cart(self.item)
    self.add_button.visible = False
    self.added_button.visible = True
        
