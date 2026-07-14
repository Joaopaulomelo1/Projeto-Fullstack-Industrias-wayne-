from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from extensions import db
from models import Resource

resources_bp = Blueprint('resources', __name__)

def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        if session.get('role') not in ['admin', 'manager']:
            flash('Acesso negado. Apenas gerentes e admins podem fazer isso.', 'error')
            return redirect(url_for('resources.index'))
        return f(*args, **kwargs)
    return decorated

@resources_bp.route('/resources')
@login_required
def index():
    category = request.args.get('category', '')
    status = request.args.get('status', '')

    query = Resource.query
    if category:
        query = query.filter_by(category=category)
    if status:
        query = query.filter_by(status=status)

    resources = query.order_by(Resource.id.desc()).all()
    return render_template('resources.html', resources=resources,
                           category=category, status=status, role=session.get('role'))

@resources_bp.route('/resources/add', methods=['GET', 'POST'])
@admin_required
def add():
    if request.method == 'POST':
        resource = Resource(
            name=request.form['name'],
            category=request.form['category'],
            status=request.form['status'],
            description=request.form['description']
        )
        db.session.add(resource)
        db.session.commit()
        flash('Recurso adicionado com sucesso!', 'success')
        return redirect(url_for('resources.index'))
    return render_template('resource_form.html', action='add', resource=None, role=session.get('role'))

@resources_bp.route('/resources/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit(id):
    resource = Resource.query.get_or_404(id)
    if request.method == 'POST':
        resource.name = request.form['name']
        resource.category = request.form['category']
        resource.status = request.form['status']
        resource.description = request.form['description']
        db.session.commit()
        flash('Recurso atualizado!', 'success')
        return redirect(url_for('resources.index'))
    return render_template('resource_form.html', action='edit', resource=resource, role=session.get('role'))

@resources_bp.route('/resources/delete/<int:id>', methods=['POST'])
@admin_required
def delete(id):
    resource = Resource.query.get_or_404(id)
    db.session.delete(resource)
    db.session.commit()
    flash('Recurso removido.', 'success')
    return redirect(url_for('resources.index'))