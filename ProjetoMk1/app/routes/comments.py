from flask import Blueprint, request, jsonify
from app import db
from app.models.comment import Comment
from flask_login import login_required, current_user

bp = Blueprint('comments', __name__, url_prefix='/comments')

@bp.route('/<int:project_id>', methods=['POST'])
@login_required
def add_comment(project_id):
    data = request.json
    comment = Comment(content=data['content'], user_id=current_user.id, project_id=project_id)
    db.session.add(comment)
    db.session.commit()
    return jsonify({'message': 'Comentado'})