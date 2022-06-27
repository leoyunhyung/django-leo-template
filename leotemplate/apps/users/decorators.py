# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg import openapi


def signup_decorator(title='', request_body=None):
    return dict(
        operation_id=_('회원가입'),
        operation_description=_(
            '## < 회원가입 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. parameter 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )


def login_decorator(title='', request_body=None):
    return dict(
        operation_id=_('로그인'),
        operation_description=_(
            '## < 로그인 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. parameter 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={200: openapi.Response(_('ok'))},
        tags=[_(f'{title}')]
    )


def me_decorator(title='', serializer=None):
    return dict(
        operation_id=_('마이페이지'),
        operation_description=_(
            '## < 마이페이지 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')]
    )


def withdraw_decorator(title='', request_body=None):
    return dict(
        operation_id=_('회원탈퇴'),
        operation_description=_(
            '## < 회원탈퇴 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. parameter 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={204: openapi.Response(_('no content'))},
        tags=[_(f'{title}')]
    )
