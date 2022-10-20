from fastapi import FastAPI

app = FastAPI(
    title="Test Application",
    description="Test Application API",
    redoc_url=None
)


@app.get("/")
async def index():
    """
        docstring
    """
    return "INDEX"
