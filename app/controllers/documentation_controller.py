from flask import Blueprint, request, jsonify
from app import db
from app.models.documentation import Documentation, DocumentationLang
from flask_jwt_extended import jwt_required

documentation_bp = Blueprint('documentation_bp', __name__)

@documentation_bp.route('/documentation', methods=['POST'])
@jwt_required()
def create_documentation():
    data = request.get_json()
    new_doc = Documentation(
        doc_id=data['doc_id'],
        name=data['name'],
        short_description=data.get('short_description'),
        active=data.get('active', True),
        order=data.get('order', 0),
        category=data.get('category')
    )
    db.session.add(new_doc)
    db.session.commit()
    return jsonify({'message': 'Documentation created successfully'}), 201

@documentation_bp.route('/documentation/<int:id>', methods=['GET'])
@jwt_required()
def get_documentation(id):
    doc = Documentation.query.get_or_404(id)
    return jsonify({
        'doc_id': doc.doc_id,
        'name': doc.name,
        'short_description': doc.short_description,
        'active': doc.active,
        'order': doc.order,
        'category': doc.category,
        'date_add': doc.date_add,
        'date_upd': doc.date_upd
    })

@documentation_bp.route('/documentation_lang', methods=['POST'])
@jwt_required()
def create_documentation_lang():
    data = request.get_json()
    new_doc_lang = DocumentationLang(
        doc_id=data['doc_id'],
        content=data['content']
    )
    db.session.add(new_doc_lang)
    db.session.commit()
    return jsonify({'message': 'DocumentationLang created successfully'}), 201

@documentation_bp.route('/documentation_lang/<int:id>', methods=['GET'])
@jwt_required()
def get_documentation_lang(id):
    doc_lang = DocumentationLang.query.get_or_404(id)
    return jsonify({
        'id': doc_lang.id,
        'doc_id': doc_lang.doc_id,
        'content': doc_lang.content
    })
