from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from extensions import db  # <-- mudou aqui
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

def create_admin():
    if not User.query.first():
        admin = User(
            username='bruce.wayne',
            password=generate_password_hash('gotham123'),
            role='admin'
        )
        db.session.add(admin)
        db.session.commit()

@auth_bp.route('/', methods=['GET', 'POST'])
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    create_admin()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            return redirect(url_for('dashboard.index'))
        else:
            flash('Usuário ou senha incorretos.', 'error')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))