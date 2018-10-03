import webapp2
import requests

from requests.auth  import HTTPDigestAuth
import json

url ="http://iamhere-172709.appspot.com/pong/"

#myRequest = requests.get(url,'')



class MainPage(webapp2.RequestHandler):
    def write_file(self):
        f = open("demofile.txt", "a")
        f.write("Now the file has one more line! \n")

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
        write_file()




app = webapp2.WSGIApplication([
    ('/ihereapi/.*', MainPage),
], debug=True)

