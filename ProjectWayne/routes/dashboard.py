from flask import Blueprint, render_template, session, redirect, url_for
from models import User, Resource

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    total_users = User.query.count()
    total_resources = Resource.query.count()
    available = Resource.query.filter_by(status='available').count()
    maintenance = Resource.query.filter_by(status='maintenance').count()
    deployed = Resource.query.filter_by(status='deployed').count()

    recent_resources = Resource.query.order_by(Resource.id.desc()).limit(5).all()

    return render_template('dashboard.html',
        username=session['username'],
        role=session['role'],
        total_users=total_users,
        total_resources=total_resources,
        available=available,
        maintenance=maintenance,
        deployed=deployed,
        recent_resources=recent_resources
    )

