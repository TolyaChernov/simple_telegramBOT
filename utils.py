from peewee import *

db = SqliteDatabase("db_weld.db")


class Weld_Pos(Model):
    pos_id = PrimaryKeyField(unique=True)
    pos_short = CharField()
    pos_long = CharField()

    class Meta:
        database = db


class Weld_Meth(Model):
    meth_id = PrimaryKeyField(unique=True)
    meth_short = CharField()
    meth_long = CharField()

    class Meta:
        database = db


# Функция вывода
def f_pos(word1: str):
    i = Weld_Pos.get(Weld_Pos.pos_short == word1)
    return str(i.pos_long)


def f_meth(word1: str):
    i = Weld_Meth.get(Weld_Meth.meth_short == word1)
    return str(i.meth_long)


db.close()
