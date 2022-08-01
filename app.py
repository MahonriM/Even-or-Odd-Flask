from flask import Flask,render_template,request
app=Flask(__name__,static_folder='templates')
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        num=int(request.form['txtnum'])
        if num%2==0:
            res="even"
            return render_template("index.html",num=num,res=res)
        else:
            res="odd"
            return render_template("index.html",num=num,res=res)
    else:
        return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)