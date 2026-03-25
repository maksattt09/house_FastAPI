from fastapi import FastAPI
from mysite.api import auth, user, property, review
import uvicorn
from mysite.admin.setup import setup_admin
from mysite.api import predict_price



house_app = FastAPI(title='Store Project')
house_app.include_router(user.user_router)
house_app.include_router(property.property_router)
house_app.include_router(review.review_router)
house_app.include_router(predict_price.predict_router)
house_app.include_router(auth.auth_router)
setup_admin(house_app)


if __name__ == '__main__':
    uvicorn.run(house_app, host='127.0.0.1', port=8006)

