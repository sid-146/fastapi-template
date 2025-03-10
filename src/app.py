"""
@author: https://github.com/sid-146

Starting Point of the API
Complete Setup and Heads
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.status import *

from api.routes import router
from core.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)
app.include_router(router, prefix=settings.API_V1_STR)


@app.get("/")
def read_root() -> HTMLResponse:
    return HTMLResponse(
        """<html>
    <head>
        <meta http-equiv="refresh" content="0; url='/docs'" />
    </head>
    <body>
        <p>If you are not redirected, <a href="/docs">click here</a> to go the documentation</p>
    </body>
</html>""",
        status_code=HTTP_301_MOVED_PERMANENTLY,
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(**settings.server_start_config)
