from flask import Blueprint, send_file, jsonify, render_template_string, request, make_response
from flask_cors import cross_origin

from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from ..service.cards import CardsManager


card_bp = Blueprint(
    'cards',
    url_prefix="/cards",
    import_name=__name__
)


@card_bp.get("/make")
@cross_origin(headers=['Authorization'], supports_credentials=True)
@jwt_required()
def make_card():
    username = get_jwt_identity()
    result = CardsManager.make_wish(username)
    if not result:
        return {"status": "already exists"}, 409

    return {'status': 'okay'}, 200


@card_bp.get("/read")
@cross_origin(headers=['Authorization'], supports_credentials=True)
@jwt_required()
def read_card():
    username = get_jwt_identity()
    result = CardsManager.get_card(username)
    if not result:
        return {"status": "there's no image yet"}, 404

    return result, 200
