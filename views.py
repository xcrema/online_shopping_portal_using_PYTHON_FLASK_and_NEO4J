from model import *
from flask import request, session, redirect, url_for, abort, render_template, flash, Flask


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods = ['GET', 'POST'])
def showsignup():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        uname = request.form['uname']
        dob = request.form['d.o.b']
        email = request.form['email']
        passw = request.form['password']
        contact = request.form['contact']
        pin = request.form['pincode']
        city = request.form['city']
        address = request.form['address']

        if len(uname) < 1:
            flash('Your Username must be at least one character long!')
        elif len(passw) < 5:
            flash('Your Password must be at least 5 characters!')
        elif User(uname).register(fname, lname, dob, email, contact, pin, city, address, passw):
            session['username'] = uname
            return render_template('index.html')
        else:
            flash('Username already exists!!')
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def showlogin():
    if request.method == 'POST':
        uname = request.form['uname']
        passw = request.form['password']
        if not User(uname).verify_password(passw):
            return 'Invalid Login'
        else:
            session['username'] = uname
            flash('Logged in.')
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/profile', methods=['GET', 'POST'])
def showprofile():
    username = session.get('username')
    if username:
        user = User(username).find()
        data = [user['fname'], user['lname'],username, user['dob'], user['email'], user['contact'], user['pin'], user['city'], user['address']]
        return render_template('view.html', data=data)
    else:
        return 'Login First'


@app.route('/setting', methods=['GET', 'POST'])
def showsettings():
    if request.method == 'POST':
        old_pass = request.form['oldpassword']
        new_pass1 = request.form['newpassword']
        new_pass2 = request.form['retype']
        username = session.get('username')
        user = User(username).find()
        if user['password'] == old_pass:
            if new_pass1 == new_pass2:
                User(username).change_pass(username, new_pass1)
                return 'Password Changed'
            else:
                return 'New Password not Matched!!'
        else:
            return 'Password is Incorrect'
    return render_template('settings.html')


@app.route('/delete', methods=['GET', 'POST'])
def showdelete():
    if request.method == 'POST':
        password = request.form['password']
        username = session.get("username")
        user = User(username).find()
        if user['password'] == password:
            User(username).dlte()
            return 'Successfully Deleted'
        else:
            return 'Invalid Password'
    return render_template('final delete.html')

@app.route('/product', methods=['POST','GET'])
def showproduct():
    return render_template('product.html')


@app.route('/beauty', methods=['POST','GET'])
def showbeauty():
	return render_template('beauty.html')


@app.route('/cart', methods=['POST','GET'])
def showcart():
	return render_template('cart.html')


@app.route('/book', methods=['POST','GET'])
def showbook():
	return render_template('book.html')


@app.route('/electronics', methods=['POST','GET'])
def showelectronics():
	return render_template('electronics.html')


@app.route('/home', methods=['POST','GET'])
def showhome():
	return render_template('product.html')


@app.route('/men', methods=['POST','GET'])
def showmen():
	return render_template('men.html')


@app.route('/op', methods=['POST','GET'])
def showonly():
	return render_template('op.html')


@app.route('/success', methods=['POST','GET'])
def showsuccess():
	return render_template('success.html')


@app.route('/women', methods=['POST','GET'])
def showwomen():
	return render_template('women.html')


if __name__ == '__main__':
    app.run(debug="True")
