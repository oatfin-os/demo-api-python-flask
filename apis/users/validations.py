from apis.base.errors import errors


def validate_user(username, password, for_login=False):
    validation_errors = {}

    if not username:
        validation_errors['username'] = "Username is required."
    if not password:
        validation_errors['password'] = "Password is required."

    if not for_login and password and len(password) < 8:
        validation_errors['password'] = "Password must be 8 characters minimum."

    if validation_errors:
        raise errors.BadRequestParameter(str(validation_errors))
