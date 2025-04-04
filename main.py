from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Optional: If you're calling the backend from the Vite dev server or a different domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your dev domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

# Example test route
@app.get("/api/test")
def test_route():
    return {"message": "Hello from FastAPI!"}

# Below: only needed if you want to serve your built Lovable.ai UI from the same backend
# Suppose your "dist" folder is at the same level as "main.py"
# after you run `npm run build` in your Lovable.ai UI code
app.mount("/", StaticFiles(directory="dist", html=True), name="static")
