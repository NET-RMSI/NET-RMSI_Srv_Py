from flask import Flask, render_template, request 
from modules.req.EventLogging import EventLogger

webapp = Flask(__name__)
test = ('test', 'test2')

@webapp.route("/", methods=["GET", "POST"])
def Index():
    print(request.form.get("serverip"))
    
    return render_template('index.html', serverip=test)


        
        
    
        
    

