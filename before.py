"""
Imagine you are asked to deliver comprehensive software dedicated for cashier in rapidly growing retail enterprise.  
You need to write code, that will allow to evaluate total value of items in basket.  
Below you can find interfece that needs to be implemented in order to provide seamless integration 
with core and third party applications that are in place within organization. 
You may need also to extend and/or refactor test case provided by Product Owner.
"""
import uuid
import typing 

class Basket:
  def __init__(self):
    pass

  def add(self, item: object, quantity: float)-> typing.NoReturn:
    raise Exception("NotImplemented")
    

  
  def remove(self, item: object, quantity: float)-> typing.NoReturn: 
    raise Exception("NotImplemented")

  @property
  def total_value(self):
     raise Exception("NotImplemented")




basket = Basket()
items = [(('beef',1000),0.75),
         (('spam',10),1),
         (('egg', 6),7*8),
         (('ham', 10),1),
         (('colored pencils in a box', 98),1)]


for item in items:  
  basket.add(item[0], item[1])

assert basket.total_value == sum([a[0][1]*a[1] for a in items])