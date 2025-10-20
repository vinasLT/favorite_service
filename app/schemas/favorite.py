from enum import Enum

from pydantic import BaseModel, Field

class Auctions(str, Enum):
    COPART = "copart"
    IAAI = "iaai"


class FavoriteIn(BaseModel):
    lot_id: int = Field(..., description="Lot ID")
    auction: Auctions = Field(..., description="Auction type")
