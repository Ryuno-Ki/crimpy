from datetime import datetime

from pony import orm

from crimpy.repositories import database as db


class TwitterModel(db.Entity):
    created_at = orm.Required(datetime)
    full_text = orm.Required(str)
    lang = orm.Required(str)
    retweeted = orm.Required(bool)
    source = orm.Required(str)