from flask import Flask
from flask import request

# Initiate the flask object
app=Flask(__name__)

# Programe has to expose to globally and any body can run the below code if they know the URL So, it should redirect to the URL.
@app.route("/")
def main():
    return "This is my first program"

@app.route("/inputurl")
def request_input():
    input=request.args.get("x")
    return "This is my input from Url {}".format(input)

if __name__=="__main__":
    app.run("0.0.0.0")

# print("Hello world")