from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi_mcp import FastApiMCP

app = FastAPI()

@app.post( 
    "/add",
    operation_id="add_two_numbers", # MCP Client gets this
    summary="ADDING 2 NUMBERS", # MCP Client gets this
    description="This adds two numbers..." # MCP Client gets this
)
async def add(a: float, b: float):
    return a + b 

@app.post( 
    "/multiply",
    operation_id="multiply_two_numbers", # MCP Client gets this
    summary="multiply two numbers..", # MCP Client gets this
    description="multiply two numbers..." # MCP Client gets this
)
async def multiply(a: float, b: float):
    return a * b 


@app.post(
    "/divide",
    operation_id="divide_two_numbers",
    summary="Divide two numbers",
    description="Divides two numbers, returning an error if the denominator is zero."
)
async def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return a / b


mcp = FastApiMCP(app)
mcp.mount()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
