from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Link
from app.schemas import LinkCreate, LinkResponse

router = APIRouter(prefix="/links", tags=["links"])

@router.post("/", response_model=LinkResponse, status_code=201)
def create_link(payload: LinkCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    data["url"] = str(data["url"])
    link = Link(**data)
    db.add(link)
    db.commit()
    db.refresh(link)
    return link

@router.get("/", response_model=list[LinkResponse])
def get_links(db: Session = Depends(get_db)):
    return db.query(Link).all()

@router.get("/{link_id}", response_model=LinkResponse)
def get_link(link_id: int, db: Session = Depends(get_db)):
    link = db.query(Link).filter(Link.id == link_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return link

@router.delete("/{link_id}", status_code=204)
def delete_link(link_id: int, db: Session = Depends(get_db)):
    link = db.query(Link).filter(Link.id == link_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    db.delete(link)
    db.commit()