from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import AdminUser, Enquiry
from ..schemas import EnquiryCreate, EnquiryOut
from ..security import current_admin

router = APIRouter(prefix="/api/enquiries", tags=["enquiries"])


@router.post("", response_model=EnquiryOut, status_code=status.HTTP_201_CREATED)
def create_enquiry(payload: EnquiryCreate, db: Session = Depends(get_db)):
    enquiry = Enquiry(**payload.model_dump())
    db.add(enquiry)
    db.commit()
    return enquiry


@router.get("", response_model=list[EnquiryOut])
def list_enquiries(db: Session = Depends(get_db), _: AdminUser = Depends(current_admin)):
    return db.scalars(select(Enquiry).order_by(Enquiry.created_at.desc())).all()
