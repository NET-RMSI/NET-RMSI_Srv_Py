from flask import Flask, render_template
from flask import request
from modules.req.EventLogging import *

webapp = Flask(__name__)

@webapp.route("/")
def index():
    processuserinput(request.args.get("serverlist"))
    
    return render_template('index.html')

def processuserinput(userinput):
    if(userinput == ""):
        LOGEVENTS_DEBUG("Nothing recieved from webapp")
    
    else:
        LOGEVENTS_DEBUG("Data recieved: " + userinput)
        
        
    
        
    

