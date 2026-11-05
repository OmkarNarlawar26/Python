# from app.init import auth
# from app.models.user import User
# from werkzeug.security import check_password_hash
#
# @auth.verify_password
# def verify_password(email, password):
#     user = User.query.filter_by(email=email).first()
#     if not user or not check_password_hash(user.password, password):
#         return False
#     return True

from app.init import auth
from app.models.user import User
from werkzeug.security import check_password_hash

@auth.verify_password
def verify_password(email, password):
    print("VERIFY_PASSWORD FUNCTION CALLED!")

    user = User.query.filter_by(email=email).first()

    if not user:
        print("User not found")
        return False

    if not check_password_hash(user.password, password):
        print("Incorrect password")
        return False

    print("Authentication successful")
    return True

print("AUTH.PY FILE LOADED!")