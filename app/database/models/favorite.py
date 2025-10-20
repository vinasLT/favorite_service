from datetime import datetime, timezone

from sqlalchemy import DateTime, Enum, func, text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models import Base
from app.schemas.favorite import Auctions


class Favorite(Base):
    __tablename__ = "favorites"

    id: Mapped[int] = mapped_column(primary_key=True)
    lot_id: Mapped[int] = mapped_column(nullable=False)
    auction: Mapped[Auctions] = mapped_column(Enum(Auctions),nullable=False)
    user_uuid: Mapped[str] = mapped_column(nullable=False)

    #lot_data
    title: Mapped[str] = mapped_column(nullable=True)
    auction_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    vin: Mapped[str] = mapped_column(nullable=True)
    images: Mapped[str] = mapped_column(nullable=True)
    odometer: Mapped[int] = mapped_column(nullable=True)
    location: Mapped[str] = mapped_column(nullable=True)
    damage: Mapped[str] = mapped_column(nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )




