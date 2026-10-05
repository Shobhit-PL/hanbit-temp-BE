from sqlalchemy import select
from sqlalchemy.orm import Session

from .config import settings
from .models import AdminUser, Testimonial
from .security import hash_password

SAMPLE = [
    ("Aarav Mehta", "Founder", "Nimbus Retail", "HanbitAI helped us transform our idea into a working AI-powered product.", 5, 12),
    ("Sofia Alvarez", "Head of Operations", "Larkspur Logistics", "Their support agent now resolves most routine tickets before our team even logs in.", 5, 47),
    ("Daniel Kim", "CTO", "Brightpath Health", "Clean Angular code, a solid FastAPI backend, and a team that explains every decision.", 5, 33),
    ("Priya Nair", "Data Analyst", "Career switcher", "The AI course had me building a working agent in the second week. I got a new job from it.", 5, 5),
    ("Marcus Webb", "Product Manager", "Orbit Labs", "They shipped our mobile app on schedule and the AI features worked from day one.", 4, 15),
    ("Hana Sato", "Co-founder", "Koto Studio", "We went from a rough brief to a live site with booking automation in six weeks.", 5, 45),
]


def seed(db: Session) -> None:
    if not db.scalar(select(AdminUser).limit(1)):
        db.add(AdminUser(email=settings.admin_email, password_hash=hash_password(settings.admin_password)))
    if not db.scalar(select(Testimonial).limit(1)):
        for name, role, company, quote, rating, img in SAMPLE:
            db.add(Testimonial(name=name, role=role, company=company, quote=quote, rating=rating,
                               image_url=f"https://i.pravatar.cc/160?img={img}"))
    db.commit()
