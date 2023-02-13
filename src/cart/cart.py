class Cart:
    def __init__(self, request):
        self.session = request.session
        # getting the session or obtaining existing session
        cart = self.session.get("session_key")
        # checking if session_key is available in the  request
        # in other words checking if the user has any cookie or session or
        # if she or he visiting the website for the first time then
        # generate a session key for the new user
        if "session_key" not in request.session:
            # creating new session for the new user
            cart = self.session["session_key"] = {}

        self.cart = cart

    def add(self, product, product_qty):
        product_id = str(product.id)
        if product_id in self.cart:
            # here self.cart is equivalent self.session.get("session_key")
            # in other words self.cart itself is the session_key dictionary
            # if product is already in cart we will update the quantity of the product
            self.cart[product_id]["qty"] = product_qty

        else:
            # otherwise we need to create a new dictionary within the cart /self.session.get("session_key") dictionary
            # with the product_id
            # and product_id dictionary contains the product price and quantity
            self.cart[product_id] = {"price": str(product.price), 'qty': product_qty}

        self.session.modified = True


# note: this is how we can get session data in django shell

# mark: here first we need to get the session key from the browse

# - and then follow the next steps

# >>> from django.contrib.sessions.models import Session
# >>> session_key = Session.objects.get(pk='vo8d449aela661rc7ylw493zpbjysccu')
# >>> session_key.get_decoded()
# note: the following code is the result
# {'session_key': {}, '_auth_user_id': '1', '_auth_user_backend': 'django.contrib.auth.backends.ModelBackend', /
# '_auth_user_hash': '0de5763a758d34e5024d3b6ca65bd46f4aff9f9f6623f88adca360f50898413b'}
