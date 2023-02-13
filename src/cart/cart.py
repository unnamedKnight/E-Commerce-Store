class Cart:

    def __init__(self, request):
        self.session = request.session
        # getting the session or obtaining existing session
        cart = self.session.get('session_key')
        # checking if session_key is available in the  request
        # in other words checking if the user has any cookie or session or
        # if she or he visiting the website for the first time then
        # generate a session key for the new user
        if "session_key" not in request.session:
            # creating new session for the new user
            cart = self.session['session_key'] = {}

        self.cart = cart