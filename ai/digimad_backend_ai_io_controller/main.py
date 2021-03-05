from fastapi import FastAPI
from app.api.router import router
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse


def init_app() -> FastAPI:
    application = FastAPI(title="HDYFT RestAPI", version="0.0.1")
    application.include_router(router)

    application.add_middleware(
        CORSMiddleware,
        allow_methods=['POST', 'GET', 'PUT', 'OPTIONS', 'DELETE'],
        allow_headers=["*"],
        allow_credentials=True,
        allow_origins=["*"],
    )

    return application


@router.get('/')
def index():
    url = 'https://10.128.14.10:31800/docs'
    response = RedirectResponse(url=url)
    return response


app = init_app()
