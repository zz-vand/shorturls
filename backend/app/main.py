from fastapi import FastAPI, HTTPException, Path, Response, status
from pydantic import BaseModel
from app.services.links_service import NewLinkService
from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["PUT", "GET", "POST", "DELETE"], 
    allow_headers=["*"],
)
new_link_service = NewLinkService()

class PutLink_user(BaseModel):
    link: str
    userword: str

class PutLink_rand(BaseModel):
    link: str

class Result(BaseModel):
    link: str
    qr: bytes



def _service_link_to_real(new_link: str) -> str:
    return f"localhost:8000/{new_link}"

@app.put("/link/random")
async def put_link_rand(put_link_request: PutLink_rand) -> Response:
    new_link = await new_link_service.put_link_rand(put_link_request.link)
    return Response(
        content=new_link["qr"],
        media_type="image/png",
        headers={"Content-Disposition": f"inline; filename=qr_{new_link['new_link']}.png"}
    )

@app.put("/link/created_by_user")
async def put_link_created_by_user(put_link_request: PutLink_user) -> Response:
    new_link = await new_link_service.put_link_user(put_link_request.link, put_link_request.userword)
    return Response(
        content=new_link["qr"],
        media_type="image/png",
        headers={"Content-Disposition": f"inline; filename=qr_{new_link['new_link']}.png"}
    )

@app.get("/{link}")
async def get_link(link: str) -> str:
    user_link = await new_link_service.get_user_link(link)

    if user_link is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="link not found")

    return Response(status_code=status.HTTP_301_MOVED_PERMANENTLY, headers={"Location": user_link})