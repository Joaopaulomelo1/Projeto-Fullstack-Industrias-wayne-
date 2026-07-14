from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from extensions import db
from models import User
from werkzeug.security import generate_password_hash

users_bp = Blueprint('users', __name__)

def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        if session.get('role') != 'admin':
            flash('Acesso restrito a administradores.', 'error')
            return redirect(url_for('dashboard.index'))
        return f(*args, **kwargs)
    return decorated

@users_bp.route('/users')
@admin_required
def index():
    users = User.query.order_by(User.id).all()
    return render_template('users.html', users=users, role=session.get('role'))

@users_bp.route('/users/add', methods=['GET', 'POST'])
@admin_required
def add():
    if request.method == 'POST':
        if User.query.filter_by(username=request.form['username']).first():
            flash('Nome de usuário já existe.', 'error')
        else:
            user = User(
                username=request.form['username'],
                password=generate_password_hash(request.form['password']),
                role=request.form['role']
            )
            db.session.add(user)
            db.session.commit()
            flash('Usuário criado com sucesso!', 'success')
            return redirect(url_for('users.index'))
    return render_template('user_form.html', action='add', user=None)

@users_bp.route('/users/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.role = request.form['role']
        if request.form['password']:
            user.password = generate_password_hash(request.form['password'])
        db.session.commit()
        flash('Usuário atualizado!', 'success')
        return redirect(url_for('users.index'))
    return render_template('user_form.html', action='edit', user=user)

@users_bp.route('/users/delete/<int:id>', methods=['POST'])
@admin_required
def delete(id):
    if id == session.get('user_id'):
        flash('Você não pode remover sua própria conta.', 'error')
        return redirect(url_for('users.index'))
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Usuário removido.', 'success')
    return redirect(url_for('users.index'))