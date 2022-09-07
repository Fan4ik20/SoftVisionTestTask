from fastapi import Request, status
from fastapi.responses import JSONResponse

from fastapi_jwt_auth.exceptions import AuthJWTException

from exceptions import exc

from schemas.enums import AvailablePlaces


def object_with_given_attr_exist_handler(
        _: Request, exc_: exc.ObjectWithGivenAttrExist
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            'detail':
                f'{exc_.name} object with given {exc_.attr} already exist.'
        }
    )


def not_valid_login_data_handler(
        _: Request, exc_: exc.NotValidLoginData
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            'detail': f'Error during login, wrong {exc_.attr} was submitted',
            'place': AvailablePlaces.body
        }
    )


def cant_perform_this_handler(
        _: Request, exc_: exc.CantPerformThis
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={'detail': exc_.action}
    )


def object_not_exist_handler(
        _: Request, exc_: exc.ObjectNotExist
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            'detail': f'{exc_.name} object with given identifier not found',
            'place': AvailablePlaces.path
        }
    )


def authjwt_exception_handler(_: Request, exc_: AuthJWTException):
    return JSONResponse(
        status_code=exc_.status_code,
        content={'detail': exc_.message}
    )
