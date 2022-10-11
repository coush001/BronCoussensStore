from ._anvil_designer import CartTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import stripe.checkout

class Cart(CartTemplate):
  def __init__(self, items, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.order = []
    self.items = items

    if not self.items:
      self.empty_cart_panel.visible = True
      self.column_panel_1.visible = False
    
    self.repeating_panel_1.items = self.items
    
    self.subtotal = sum(item['product']['price'] * item['quantity'] for item in self.items)
    self.subtotal_label.text = f"${self.subtotal:.02f}"
    
    if self.subtotal >= 35: #free shipping for orders over $35
      self.shipping_label.text = 'FREE'     
    else: #add $5 shipping
      self.shipping_label.text = "$5.00"
      self.subtotal = self.subtotal + 5
      
    self.total_label.text = f"${self.subtotal:.02f}"
      

  def shop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().shop_link_click()

  def checkout_button_click(self, **event_args):
    """This method is called when the button is clicked"""  
    for i in self.items:
      self.order.append({'name':i['product']['name'], 'quantity':i['quantity']})
    try:
      charge = stripe.checkout.charge(amount=self.subtotal*100,
                                      currency="USD",
                                      shipping_address=True,
                                      title="Cupcakes & Co.",
                                      icon_url="_/theme/cupcake_logo.png")
    except:
      return
    
    anvil.server.call('add_order', charge['charge_id'], self.order)

    get_open_form().cart_items = []
    get_open_form().cart_link_click()
    Notification("Your order has been received!").show()


  

