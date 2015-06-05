__all__ = ['get_user_token']

from calendar import timegm
from datetime import datetime

from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


def get_user_token(credentials):
    user = authenticate(**credentials)
    payload = jwt_payload_handler(user)

    if api_settings.JWT_ALLOW_REFRESH:
            payload['orig_iat'] = timegm(
                datetime.utcnow().utctimetuple()
            )

    token = jwt_encode_handler(payload)

    return token
