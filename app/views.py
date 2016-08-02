from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from app.forms import LoginForm
from app.models import User


# @lm.user_loader
# def load_user(id):
#     return User.query.get(int(id))
#
#
# @app.before_request
# def before_request():
#     g.user = current_user

@app.route('/')
@app.route('/index')
def index():
    # user = g.user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           posts=posts,
                           name=session.get('name'),
                           known=session.get('known', False))


#
#
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.loginname.data).first()
        if user is None:
            user = User(username=form.loginname.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.loginname.data
        form.loginname.data = ''
        return redirect(url_for('index'))
    return render_template('login.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))


@app.route('/logout')
def logout():
    session['name'] = None
    return redirect(url_for('index'))


@app.route('/profile')
def profile():
    return render_template('profile.html', name=session.get('name'))

#
# @oid.after_login
# def after_login(resp):
#     if resp.email is None or resp.email == "":
#         flash('Invalid login. Please try again.')
#         return redirect(url_for('login'))
#     user = User.query.filter_by(email=resp.email).first()
#     if user is None:
#         nickname = resp.nickname
#         if nickname is None or nickname == "":
#             nickname = resp.email.split('@')[0]
#         user = User(nickname=nickname, email=resp.email)
#         db.session.add(user)
#         db.session.commit()
#     remember_me = False
#     if 'remember_me' in session:
#         remember_me = session['remember_me']
#         session.pop('remember_me', None)
#     login_user(user, remember=remember_me)
#     return redirect(request.args.get('next') or url_for('index'))


# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))
