from flask import Flask, render_template

# initialize instance of WSGI application
# act as a central registry for the view functions, URL rules, template configs
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)