from cofi import app
from flask import render_template,request
from productoinfo import Product

message=''
@app.route('/')
@app.route('/product/save',methods=['GET'])
def ecomlanddingpage():
    message='welcome to landing page'
    return render_template('index.html',message=message)

productlist=[]
@app.route('/product/save',methods=['GET','POST'])
def saveupdate():
    if request.method=="POST":
        formdata=request.form()
        product(pid=formdata.get('pid'),
                pnm=formdata.get('pnm'),
                prc=formdata.get('prc'),
                pven=formdata.get('pven'),
                pqty=formdata.get('pqty')
                )
        productlist.append(product)
    return render_template('addupdate.html')


@app.route('/product/delete',methods=['POST'])
def delete():
    pass


@app.route('/product/edit',methods=['POST'])
def edit():
    pass


@app.route('/product/show',methods=['POST'])
def showall():
    pass

@app.route('/product/search',methods=['POST'])
def search():
    pass

if __name__=='__main__':
    app.run(debug=True)