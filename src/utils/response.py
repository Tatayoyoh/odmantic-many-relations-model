from fastapi.responses import JSONResponse

SUCCESS_RESPONSE = {'success': True}
ERROR_RESPONSE = {'success': False, 'description': ''}
NOTFOUND_RESPONSE = ERROR_RESPONSE | {"description": "Unknow request or entity"}
CLIENTERROR_RESPONSE = ERROR_RESPONSE | {"description": "Request error"}
SERVERERROR_RESPONSE = ERROR_RESPONSE | {"description": "Internal server error"}

class ErrorResponse(JSONResponse):
    code = 500
    response = ERROR_RESPONSE
    def __init__(self, description='') -> None:
        if description:
            self.response['description'] = str(description)
        super().__init__(self.response, status_code=self.code)

class Error(ErrorResponse):
    code = 400
    response = CLIENTERROR_RESPONSE

class NotFound(ErrorResponse):
    code = 404
    response = NOTFOUND_RESPONSE

class ServerError(ErrorResponse):
    code = 500
    response = SERVERERROR_RESPONSE