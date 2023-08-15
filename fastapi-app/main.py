from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Add CORS middleware with allowed origins
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://34.70.238.189",
    "http://34.70.238.189:80",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ahosan")
def read_root():
    return {"message": "From Ahosan's 1st FastAPI"}
