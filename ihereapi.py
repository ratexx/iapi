import webapp2
class MainPage(webapp2.RequestHandler):
    def write_file():
        f = open("demofile.txt", "a")
        f.write("Now the file has one more line!")

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
        write_file()





app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
