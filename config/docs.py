# Django
from django.conf import settings
from django.urls import include, path
from django.utils.translation import ugettext_lazy as _

# Django Rest Framework
from rest_framework import permissions

# Third party
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

description = _(
    """
백엔드 서버 API 문서입니다.

# Response Data

```json
{
    "code": " ... ",
    "message": " ... ",
    "result": { ... },
    "errors": {
        "field_errors": {
            "first_field": "error_detail" ,
            "second_field": " ... ",
        },
        "non_field_errors": [
            "some_error_message",
            " ... "
        ]
    },
}
```
## 세부 안내

`code` Status 코드입니다.

`message` 상세 메시지입니다.

`result` 응답 결과 데이터입니다.

`errors` (optional) 오류 발생시 나타나는 필드입니다.

- `field_errors` 400 Bad Request 오류 메시지입니다.

- `non_field_errors` 그 외 오류 메시지입니다.

<br/>"""
)

# Only expose to public in local and development.
public = bool(settings.DJANGO_ENV in ('local',))

# Fully exposed to only for local, else at least should be staff.
if settings.DJANGO_ENV == "local":
    permission_classes = (permissions.AllowAny,)
else:
    permission_classes = (permissions.IsAdminUser,)

schema_url_patterns = [
    path(r"^api/", include("config.api_router")),
]

schema_view = get_schema_view(
    openapi.Info(
        title=_("API 문서"),
        default_version="v1",
        description=description,
        contact=openapi.Contact(email="leoyunhyung@gmail.com"),
        license=openapi.License(name="Copyright 2022. Yunhyung Leo Lee. all rights reserved."),
    ),
    public=public,
    permission_classes=permission_classes,
    patterns=schema_url_patterns,
)
