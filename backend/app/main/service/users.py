from ..model.users import User

from flask_bcrypt import generate_password_hash, check_password_hash


class UserManager:

    @staticmethod
    def _get_all_users() -> list:
        return User.objects.only('username').all()

    @staticmethod
    def _delete_all_users():
        users = User.objects().all()
        users.delete()

    @staticmethod
    def signup_user(username: str, email: str, password: str):

        user = User.objects(username=username).first()
        if user:
            return None

        hashed_password = generate_password_hash(password).decode('utf-8')

        user = User(
            username=username,
            email=email,
            hashed_password=hashed_password
        )
        user.save()

        return True

    @staticmethod
    def login_user(username: str, password: str):

        user = User.objects(username=username).first()
        if not user:
            return None

        hashed_password = check_password_hash(user.hashed_password, password)
        if not hashed_password:
            return None

        return True


if __name__ == '__main__':
    pass
