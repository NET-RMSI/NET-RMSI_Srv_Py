from flask import Flask, render_template, request 
from modules.req.EventLogging import *

webapp = Flask(__name__)

@webapp.route("/", methods=["GET", "POST"])
def index():
    print(request.form.get("serverip"))
    
    return render_template('index.html')

        
        
    
        
    

