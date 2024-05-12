from ._anvil_designer import HomeTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..About import About
from ..Product import Product

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    promotes = app_tables.products.search(promote=True)
    try: 
      self.cart = get_open_form().get_cart()
      self.cart_items = [i['product'].get_id() for i in self.cart]
    except:
      self.cart_items=False
    
    for p in promotes:
      print('User has opened home, the cart contains:', self.cart_items)
      if self.cart_items and p.get_id() in self.cart_items:
        self.flow_panel_1.add_component(Product(item=p, cart=True), width='30%')
      else:
        self.flow_panel_1.add_component(Product(item=p), width='30%')

    self.flow_panel_2.add_component(About(),full_width_row=True)

  
  def shop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().shop_link_click()


