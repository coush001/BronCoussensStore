from ._anvil_designer import CartTemplate
from anvil import *
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

    self.shipping_fee = 0 #14.99
      
    if not self.items:
      self.empty_cart_panel.visible = True
      self.column_panel_1.visible = False
    
    self.repeating_panel_1.items = self.items
    
    self.subtotal = sum(item['product']['price'] for item in self.items)
    self.subtotal_label.text = f"£{self.subtotal:.02f}"
    
    self.shipping_label.text = "£TBC"
    self.total = self.subtotal + self.shipping_fee
      
    self.total_label.text = f"£{self.subtotal:.02f}"
      

  def shop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().shop_link_click()

  def checkout_button_click(self, **event_args):
    """This method is called when the button is clicked"""  
    for i in self.items:
      self.order.append({'name':i['product']['name']})

    shipaddress = TextArea()
    alert(content=shipaddress, title='Please enter your contact email (for order dispatch updates):',large=True)
    
    try:
      charge = stripe.checkout.charge(amount=self.total*100,
                                      currency="GBP",
                                      shipping_address=True,
                                      title="B. Coussens Ceramics",
                                      )
      print('stripe success')
    except Exception as e:
      print(e.message, e.args)
      return
    
    anvil.server.call('add_order', charge['charge_id'], self.order, self.items, self.shipping_fee, self.subtotal, self.total, str(charge.items()), shipaddress.text)
          
    get_open_form().cart_items = []
    get_open_form().cart_link_click()
    
    Notification("Your order has been received!").show()


  

