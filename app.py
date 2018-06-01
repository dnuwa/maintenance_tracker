from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_in', methods=['GET','POST'])
def sign_in():
    return render_template('sign_in.html')

@app.route('/sign_up', methods = ['GET','POST'])
def sign_up():
    return render_template('sign_up.html')
    
@app.route('/user_view', methods = ['GET','POST'])
def user_view():
    return render_template('user_view.html')

@app.route('/admin_view', methods = ['GET','POST'])
def admin_view():
    return render_template('admin_view.html')
    

if __name__ == '__main__':
    app.run(debug=True)