from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
@app.route('/<name>')
def index(name=None):
    return render_template("homepage.html", name=name)

#@app.route('/lantern')
#def lantern():
 #   return "<h2> test <h2>"

#@app.route('/lantern/<username>')
#def profile(username):
 #   return "Hi there, {}".format(username)

#@app.route('/lantern/post/<int:postnumber>')
#def postID(postnumber):
 #   print(type(postnumber))
  #  return "This is the postnumber: ".format(type(postnumber))
  

if __name__ == "__main__":
    app.run()
