# Imports for iframe
from anvil.js.window import jQuery
from anvil.js import get_dom_node
from ._anvil_designer import AboutTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class About(AboutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.map_1.center = GoogleMap.LatLng(51.5374, -0.9003)
    self.map_1.zoom = 13


  def button_1_click(self, **event_args):
    print(self.map_1.map_data.to_geo_json())
    """This method is called when the button is clicked"""
    pass

