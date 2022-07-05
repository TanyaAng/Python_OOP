class ProductRepository:
    def __init__(self):
        self.products = []

    def search_product_by_name(self, product_name):
        searched_name = [p for p in self.products if p.name == product_name]
        if searched_name:
            return searched_name[0]
        return False

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        searched_product=self.search_product_by_name(product_name)
        if searched_product:
            return searched_product

    def remove(self, product_name):
        searched_product=self.search_product_by_name(product_name)
        if searched_product:
            self.products.remove(searched_product)

    def __repr__(self):
        result=''
        for p in self.products:
            result+=f"{p.name}: {p.quantity}\n"
        return result.strip()
