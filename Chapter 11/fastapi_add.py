from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/api/add")
def add_numbers(
    num1: int = Query(..., description="First number"),
    num2: int = Query(..., description="Second number"),
):
    result = num1 + num2
    return {"result": result}
