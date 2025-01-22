import uvicorn
from fastapi import FastAPI

from app.api.endpoints.user import router as user_router
from app.api.endpoints.category import router as category_router
from app.api.endpoints.product import router as product_router
from app.core.config import settings

app = FastAPI(title=settings.app_title, description=settings.description)


@app.get('/')
def main():
    return {'status': 'ok'}


app.include_router(category_router)
app.include_router(product_router)
app.include_router(user_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
