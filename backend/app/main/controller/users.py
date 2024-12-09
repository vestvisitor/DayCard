from flask import Blueprint,jsonify, request, make_response, redirect, url_for
from flask_jwt_extended import (jwt_required, unset_jwt_cookies,
                                get_jwt_identity, create_access_token,
                                set_access_cookies)
from flask_cors import cross_origin

from ..model.users import User
from ..service.users import UserManager


user_bp = Blueprint(
    'user',
    url_prefix="/users",
    import_name=__name__
)


@user_bp.get("/all")
def get_all_users_endpoint():
    users = UserManager._get_all_users()
    return jsonify(users), 200


@user_bp.get("/delete")
def delete_all_users_endpoint():
    UserManager._delete_all_users()
    return {"Kek": "removed"}


@user_bp.get("/login")
def login_user_page():

    username = request.cookies.get('username')
    user = User.objects(username=username).first()
    if user:
        return redirect(url_for('user.get_me_endpoint'))
    return '''
            <form method="post">
                <p>username: <input type=text name=username>
                <p>password <input type=text name=password>
                <p><input type=submit value=Login>
            </form>
        '''


@user_bp.post("/login")
@cross_origin()
def login_user_endpoint():

    username = request.json.get('username')
    password = request.json.get('password')

    result = UserManager.login_user(
        username = username,
        password = password
    )

    if not result:
        return "{'problem': 'problem'}", 409

    access_token = create_access_token(identity=username)
    response = jsonify({'access_token_cookie': access_token})
    set_access_cookies(response, access_token)
#
    return response, 200


@user_bp.get("/signup")
def signup_user_page():
    username = request.cookies.get('username')
    user = User.objects(username=username).first()
    if user:
        return redirect(url_for('user.me'))
    return '''
        <form method="post">
            <p>username: <input type=text name=username>
            <p>email: <input type=text name=email>
            <p>password <input type=text name=password>
            <p><input type=submit value=Signup>
        </form>
    '''


@user_bp.post("/signup")
@cross_origin()
def create_user():
    user_data = request.json

    result = UserManager.signup_user(
        username = user_data.get('username'),
        email = user_data.get('email'),
        password = user_data.get('password')
    )
    if not result:
        return {"error": "already exists"}, 409

    return {'status': 'okay'}, 200


@user_bp.get("/me")
@cross_origin(headers=['Authorization'], supports_credentials=True)
@jwt_required()
def get_me_endpoint():
    username = get_jwt_identity()
    return jsonify(foo=username)


@user_bp.post("/logout")
@cross_origin()
def logout_user():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response, 200


@user_bp.get("/test")
# @cross_origin()
def test_func():
    return "<h2>Hello, World!</h2>"
