from flask import Flask,render_template,request,redirect,session
from pymongo import MongoClient
mongouri='mongodb+srv://pavani:p12345@cluster0.h1625.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client=MongoClient('mongouri')
# print("DB connected")
app=Flask(__name__)



@app.route('/')
def home():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/signupForm',methods=["post"])
def signupForm():
    username=request.form["username"]
    password=request.form["password"]

    # data={
    #     "username":username,
    #     "password":password
    # }

    data={
        "username":pavani,
        "password":p12345
    }

    db=client["sacet"]
    collection=db["cse"]
    k=collection.find_one({"username":data["username"]})
    print(k)

    if k is not None:
        print("account exist")
        return render_template("signup.html",err="account exist")
    else:
        collection.insert_one(data)

    return render_template("signup.html",msg="account created")
if  __name__=="__main_":
    app=Flask(__name__)
    app.run(
        # host="0.0.0.0",
        host="127.0.0.1",
        port=9000,
        debug=True
    )

# print("pavani")