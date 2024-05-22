from app import db
from datetime import datetime

class Documentation(db.Model):
    __tablename__ = 'dc_documentation'
    id = db.Column(db.Integer, primary_key=True)
    doc_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    short_description = db.Column(db.String(255), nullable=True)
    active = db.Column(db.Boolean, default=True)
    order = db.Column(db.Integer, nullable=False, default=0)
    category = db.Column(db.String(255), nullable=True)
    date_add = db.Column(db.DateTime, default=datetime.utcnow)
    date_upd = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Documentation {self.name}>'

class DocumentationLang(db.Model):
    __tablename__ = 'dc_documentation_lang'
    id = db.Column(db.Integer, primary_key=True)
    doc_id = db.Column(db.Integer, db.ForeignKey('dc_documentation.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    documentation = db.relationship('Documentation', backref=db.backref('translations', lazy=True))

    def __repr__(self):
        return f'<DocumentationLang {self.id}>'
