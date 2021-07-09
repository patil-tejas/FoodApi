
from flask import render_template , request , redirect
from FoodApi import app, mysql
from .myapi import get_image_list

#get_image_list returns a list of Image Url from the pixabay API



@app.route('/')
def food_api():
    return render_template("pictures.html",image_list=get_image_list())

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
    
@app.route('/submit_form', methods = ['POST','GET'])
def submit_form():
    if request.method == 'POST':
        print("hi")
        try:
            data = request.form.to_dict()
            email = data['email']
            subject = data['subject']
            message = data['message']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users(email,subject,message) VALUES(%s, %s, %s)",(email,subject,message))
            mysql.connection.commit()
            cur.close()
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something Went Wrong!'

#the above method allows to reduce repetition of below functions

# @app.route('/about.html')
# def about():
#     return render_template("about.html")

# @app.route('/#pictures')
# def pictures():
#     return render_template("/index.html/#pictures")


