from flask import Flask, render_template,request
from werkzeug.utils import redirect
app = Flask(__name__)
@app.route('/', methods=['POST','GET'])

def sum():
    sum=''
    if request.method=='POST' and 'num1' in request.form and 'num2' in request.form:
        num1= float(request.form.get('num1'))
        num2= float(request.form.get('num2'))
        sum=num1+num2
    return render_template('base.html',sum=sum)
if __name__ == "__main__":
    app.run(debug=True)


