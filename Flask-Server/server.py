from flask import Flask,render_template,request
from try1encryption import driver
from try1decryption import decryptDriver
 
app = Flask(__name__)
 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        print(int(form_data["The Password that you entered is: "]))
        Password=int(form_data["The Password that you entered is: "])
        key= driver(Password)
        mydict={}
        mydict["Password"]= int(form_data["The Password that you entered is: "])
        mydict["Key"]= int(key)
        #form_data["Value of key"]= key
        print(mydict)
        return render_template('data.html',form_data = mydict)

@app.route('/verify')
def verify():
    return render_template('verify.html')
@app.route('/crosscheckdata/', methods = ['POST', 'GET'])
def crosscheckdata():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/verify' to submit form"
    if request.method == 'POST':
        verify_data = request.form
        print(int(verify_data["The Key that you entered is: "]))
        KeyByUser=int(verify_data["The Key that you entered is: "])
        CrossCheckPassword= decryptDriver(KeyByUser)
        revdict={}
        revdict["Key"]= int(verify_data["The Key that you entered is: "])
        revdict["Password"]= int(CrossCheckPassword)
        #form_data["Value of key"]= key
        print(revdict)
        return render_template('crosscheckdata.html',verify_data = revdict)
 
app.run(host='localhost', port=5000)






# from flask import Flask,render_template

# app= Flask(__name__)

# # @app.route("/members")
# # def members():
# #     return{"members":["1","2","3"]}

# # if __name__== "__main__":
# #     app.run(debug=True)

 
# @app.route('/form/<int:id>')
# def form(id):
#     return render_template('form.html', number=id)
 
# app.run(host='localhost', port=5000)
