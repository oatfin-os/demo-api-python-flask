from apis.base.errors.errors import BadRequestParameter


class UserExistError(BadRequestParameter):
    def __init__(self):
        msg = "A user exists with this username already."
        super(UserExistError, self).__init__(msg)


class UserNotFoundError(BadRequestParameter):
    pass


class UnauthenticatedError(BadRequestParameter):
    def __init__(self):
        self.msg = "User is not authenticated."
        self.error_code = 401


class InvalidUserError(BadRequestParameter):
    def __init__(self):
        self.msg = "Invalid username and/or password."
        self.error_code = 401
