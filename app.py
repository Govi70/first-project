print("hello world")
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("home.html")

print("Finished")

if __name__=="__main__":
  app.run(debug=True)



