from fastapi import FastAPI
import uvicorn


from routers import user_routes, product_routes

app = FastAPI()

# Routers
app.include_router(user_routes.router)
app.include_router(product_routes.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)