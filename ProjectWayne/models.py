# models.py
from extensions import db  # <-- mudou aqui

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='employee')

    def is_active(self): return True
    def is_authenticated(self): return True
    def is_anonymous(self): return False
    def get_id(self): return str(self.id)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(30), default='available')
    description = db.Column(db.String(300))