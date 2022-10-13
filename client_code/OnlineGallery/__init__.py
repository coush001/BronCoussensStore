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
        
    products = app_tables.products.search(available=True)
    for p in products:
      self.flow_panel_1.add_component(Product(item=p), width='30%')
