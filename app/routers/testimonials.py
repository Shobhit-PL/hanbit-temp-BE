from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Testimonial
from ..schemas import TestimonialOut

router = APIRouter(prefix="/api/testimonials", tags=["testimonials"])


@router.get("", response_model=list[TestimonialOut])
def list_testimonials(db: Session = Depends(get_db)):
    return db.scalars(select(Testimonial).where(Testimonial.published).order_by(Testimonial.id)).all()
