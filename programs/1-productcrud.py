"""
class Product():
    code:int
    name:str
    supplier:str
    price:int

    def info(self):
        return "code :",self.code



prod1 = Product()
prod1.code=1
prod1.name="smart phone"
prod1.supplier = "Samsung"
prod1.price = 60000
print("code ",prod1.code)
info= prod1.info()
print(info)
"""
class ProductNew():
    """
    Constructor
    """
    def __init__(self,code,name,supplier,price):
        self.code = code
        self.name = name
        self.suppier = supplier
        self.price = price

    def info(self):
        print("code ",self.code," Name ",self.name,"Supplier ",self.suppier,"Price ",self.price)
"""
prod2 = ProductNew(2,"Laptop","Lenovo",80000)
prod2.info()
"""
class ProductManagement():
    productlist=[]
    def addProduct(self,product):
        print("add product")
        self.productlist.append(product)

    def listProduct(self):
        print("list product")
        for prod in self.productlist:
            prod.info()

    def searchBySupplier(self,supplier):
        print("searchBySupplier")
        for prod in self.productlist:
            if (prod.suppier == supplier):
                prod.info()
        else:
            print("no products found for the supplier ",supplier)
    
    def searchbyPriceRange(self,min,max):
        print("searchbyPriceRange")
        for prod in self.productlist:
            if (prod.price>=min and prod.price<= max):
                prod.info()
        else:
            print("no products found for this price range ")


pm = ProductManagement()
prod1 = ProductNew(1,"TV","Sony",60000)
prod2 = ProductNew(2,"Mobile","Samsung",80000)
prod3 = ProductNew(3,"Laptop","Samsung",85000)
pm.addProduct(prod1)
pm.addProduct(prod2)
pm.addProduct(prod3)
pm.listProduct()
pm.searchBySupplier("Samsung")
pm.searchBySupplier("Apple")
pm.searchbyPriceRange(70000,80000)
