import webapp2




















class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, API!')















app = webapp2.WSGIApplication([
    ('/ihereapi/.*', MainPage),
], debug=True)
