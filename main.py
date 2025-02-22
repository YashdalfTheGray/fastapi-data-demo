from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import List

from data_module import initialize

app = FastAPI()

# initialize the graph
graph = initialize()


# pydantic models
class Status(BaseModel):
    status: str = "OK"


class StatusWithMessage(Status):
    message: str


class NodeData(BaseModel):
    foo: int
    bar: str


class NodeIDs(BaseModel):
    nodes: List[str]


class Neighbors(BaseModel):
    neighbors: List[str]


@app.get("/", include_in_schema=False)
async def root_redirect():
    return RedirectResponse(url="/api/v1")


@app.get("/api/v1", response_model=StatusWithMessage)
async def get_api_status():
    return StatusWithMessage(message="there is more here")


@app.get("/api/v1/ping", response_model=Status)
async def get_api_ping():
    return Status()


@app.get("/api/v1/nodes", response_model=NodeIDs)
async def list_nodes():
    nodes = graph.get_all_nodes()
    return NodeIDs(nodes=nodes)


@app.get("/api/v1/nodes/{node_id}", response_model=NodeData)
async def get_node_data(node_id: str):
    node_id = node_id.upper()
    data = graph.get_node_data(node_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Node not found")
    return NodeData(**data)


@app.get("/api/v1/nodes/{node_id}/neighbors", response_model=Neighbors)
async def get_node_neighbors(node_id: str):
    node_id = node_id.upper()
    if node_id not in graph.get_all_nodes():
        raise HTTPException(status_code=404, detail="Node not found")
    neighbors = graph.get_neighbors(node_id)
    return Neighbors(neighbors=neighbors)
