from ._anvil_designer import OnlineGalleryTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Product import Product

class OnlineGallery(OnlineGalleryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    available = app_tables.products.search(available=True)  
    sold = app_tables.products.search(available=False)

    try:
      self.cart = get_open_form().get_cart()
      cart_items = [i['product'].get_id() for i in self.cart]
      print('User has opened gallery, the cart contains:', cart_items)
    except:
      print('failed to get_cart')
      cart_items = False
    
    for item in available:
      if cart_items and item.get_id() in cart_items:
        self.flow_panel_1.add_component(Product(item=item, cart=True), width='90%')
      else:
        self.flow_panel_1.add_component(Product(item=item), width='90%')

    for item in sold:
      self.flow_panel_2.add_component(Product(item=item), width='30%')