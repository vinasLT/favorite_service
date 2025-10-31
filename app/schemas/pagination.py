from app.core.utils import create_pagination_page
from app.database.schemas.favorite import FavoriteRead

FavoritesPage = create_pagination_page(FavoriteRead)