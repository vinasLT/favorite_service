from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, field_validator

from app.schemas.favorite import Auctions


class FavoriteBase(BaseModel):
    lot_id: int
    auction: Auctions


    title: str | None = None
    auction_date: datetime | None = None
    vin: str | None = None
    images: str | None = None
    odometer: int | None = None
    location: str | None = None
    damage: str | None = None


class FavoriteCreate(FavoriteBase):
    user_uuid: str



class FavoriteUpdate(BaseModel):
    lot_id: Optional[int] = None
    auction: Optional[bool] = None
    user_uuid: Optional[str] = None
    title: Optional[str] = None
    auction_date: Optional[datetime] = None
    vin: Optional[str] = None
    images: Optional[str] = None
    odometer: Optional[int] = None
    location: Optional[str] = None
    damage: Optional[str] = None


class FavoriteRead(FavoriteBase):
    id: int

    images: list[str]

    @field_validator("images", mode="before")
    @classmethod
    def validate_images(cls, v):
        if v:
            return v.split(",")
        return None

    model_config = ConfigDict(from_attributes=True)
