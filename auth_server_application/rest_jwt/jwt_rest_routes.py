from flask import Blueprint, render_template, request
from flask import current_app as app
import jwt
import os
from ..decorators import login_required

jwt_rest_bp = Blueprint('jwt_rest_bp', __name__)


@jwt_rest_bp.route('/api/v1/user', methods=['POST'])
@login_required
def jwt():
    data = request.get_json()
    private_key = os.environ.get('private_key')

    return False  # FIXME later
