from flask import Flask,render_template

app=Flask(__name__)  # creating an object of Flask

@app.route("/")  # routing or setting the url
def hello_world():
    #return "<p>Hello,World!</p>"
    return render_template("home.html")    # this is how we render a template on our website

# if __name__=='__main__':     # another way of running the file on server
#     app.run(host='0.0.0.0',debug=True)  

# flask willl allow you to acces file in static through urls
# we pass dynamic info in the template though render_temlate only using {{}}
                              