from store.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_args')
        if 'session_args' not in request.session:
            self.session['session_args'] = {}
            cart = self.session['session_args']

        self.cart = cart

    def add(self, product, quantity=1):
        product_id = product.id
        if (product_id in self.cart) and (self.cart[product_id]['quantity'] + quantity <= product.quantity):
                self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {
                'name': product.name,
                'price': float(product.sale_price) if product.sale else float(product.price),
                'quantity': quantity,
            }

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quantities(self):
        return {prod_id: self.cart[prod_id]['quantity'] for prod_id in self.cart.keys()}

    def get_total(self):
        return round(sum(self.cart[prod_id]['price'] * self.cart[prod_id]['quantity'] for prod_id in self.cart.keys()), 2)

    def update(self, product_id, quantity):
        if product_id in self.cart and quantity > 0:
            self.cart[product_id]['quantity'] = quantity

        self.session.modified = True

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True


