from sqladmin import ModelView

from app.users.models import Users
from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email, Users.bookings]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"


class HotelsAdmin(ModelView, model=Hotels):
    column_list = [c.name for c in Hotels.__table__.c] + [Hotels.rooms]
    name = "Отель"
    name_plural = "Отели"
    icon = "fa-solid fa-user"


class RoomsAdmin(ModelView, model=Rooms):
    column_list = [c.name for c in Rooms.__table__.c] + [Rooms.hotel, Rooms.bookings]
    name = "Комната"
    name_plural = "Комнаты"
    icon = "fa-solid fa-user"


class BookingsAdmin(ModelView, model=Bookings):
    column_list = [c.name for c in Bookings.__table__.c] + [Bookings.user, Bookings.room]
    name = "Бронирование"
    name_plural = "Бронирования"






