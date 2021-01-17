class BadRequestParameter(Exception):
    def __init__(self, message):
        self.msg = message
        self.error_code = 400


class MissingAuthorizationHeader(BadRequestParameter):
    def __init__(self):
        msg = "Missing authorization header."
        super(MissingAuthorizationHeader, self).__init__(msg)


class ExpiredTokenError(BadRequestParameter):
    def __init__(self):
        msg = "Token authorization has expired."
        super(ExpiredTokenError, self).__init__(msg)


class UnknownServerError(Exception):
    def __init__(self):
        self.msg = "An unknown server error occurred."
        self.error_code = 500
