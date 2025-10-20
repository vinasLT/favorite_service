import factory

from app.database.models import Favorite


import factory
from factory.alchemy import SQLAlchemyModelFactory
from factory import fuzzy
from datetime import timezone

from app.database.models import Favorite
from app.schemas.favorite import Auctions


class FavoriteFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Favorite
        sqlalchemy_session = None
        sqlalchemy_session_persistence = "flush"

    lot_id = factory.Faker("random_int", min=1, max=10_000_000)
    auction = fuzzy.FuzzyChoice(list(Auctions))
    user_uuid = factory.Faker("uuid4")

    title = factory.Faker("sentence", nb_words=6)
    auction_date = factory.Faker("date_time_between", start_date="-30d", end_date="+30d", tzinfo=timezone.utc)
    vin = factory.Faker("bothify", text="#########?????????")
    images = factory.LazyFunction(lambda: "[]")
    odometer = factory.Faker("random_int", min=0, max=400000)
    location = factory.Faker("city")
    damage = factory.Faker("word")

