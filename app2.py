from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    #return "This is homepage and the method is: {}".format(request.method)
    return render_template("homepage.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return ''' <form_method = "POST"
    Language: <input type = "text", name = "language"> <br>
    Framework: <input type = "text", name = "framework"> <br>
    <input type = "submit" value"Submit the form"> <br>
</form>
    
                                                                    '''

if __name__ == "__main__":
    app.run()
