from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth_routes

app = FastAPI()

# Allow requests from your frontend origin(s)
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Allow only these origins
    allow_credentials=True,
    allow_methods=["*"],        # Allow all HTTP methods
    allow_headers=["*"],        # Allow all headers
)

app.include_router(auth_routes.router)

@app.get("/")
async def root():
    return {"message": "FastAPI backend is running!"}
