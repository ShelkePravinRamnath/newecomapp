

class Product():
    def __init__(self,pid,prnm,pqty,prc,pven):
        self.prodId=pid
        self.prodName=prnm
        slef.prodQty=pqty
        self.prodPrice=prc
        self.Vendor=pven


    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)