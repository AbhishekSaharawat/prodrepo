from flask import Flask , render_template , request 
import os
import datetime 
from  pymongo import  MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    
        app = Flask(__name__)
        #ec2-35-172-225-68.compute-1.amazonaws.com
        client = MongoClient(os.getenv("MONGODB_URI"))
        app.db = client.myblogdb
        @app.route("/")
        def hello_world():
            return "Hi this is Hello World Program"
        elements =[]

        @app.route("/login", methods=["GET", "POST"])
        def login_page():
        
            print([e for e in app.db.myCollection.find({})])
        
            #user_data ={"name":"Abhishek Saharawat", "email":"abhisheknov23@gmail.com"}
        
            if request.method == "POST" :
            
              collected_data = request.form.get("name" )
              email= request.form.get("email")
              password=request.form.get("password")
              content=request.form.get("content")
              app.db.myCollection.insert_one(
                { "name": collected_data, "email": email, "password": password ,"content":content }
                        )
              
              print (f"Name entered by user is {collected_data}")
            
         
            
            #elements.append((collected_data,email,password))
               
            elements=[ (value["name"],
                        value["email"], 
                        value["password"],
                        value["content"]
                              ) # It can be list of list instead of list of tuples because database send the cursor . So anything (list or tuple) can handle that
                        
                               for value in  app.db.myCollection.find({})]
            return render_template("index.html", elements=elements )    #render template 1 function hota h jo html files acccept 
                                                    #karta h but ye templates folder me honi chahiye .
                                                    # Flask understands only templates folder . Acha in endpoints me jo return statement hoti ha vo seedha browser ko return karti h ,
                                                    # ab chahe vo html page retun kaare ya simple string as per you condition
            #return render_template("index.html" )   
            
                                                    
        return app
