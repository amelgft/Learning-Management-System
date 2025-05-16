from flask import flash, redirect, render_template, url_for
from app import app, db
from app.forms import  RegisterForm
from app.models import User

@app.route('/' )#, methods=['GET', 'POST']
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    # This checks if the form submission is valid and method is POST
    if form.validate_on_submit(): # i need to know what is this
        user = User(name=form.name.data, email=form.email.data, username=form.username.data)
        user.set_password(form.password.data)  
        db.session.add(user)
        db.session.commit()
        
        # flash('Congratulations, you are now a registered user!') # this is  not working
        return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)


    