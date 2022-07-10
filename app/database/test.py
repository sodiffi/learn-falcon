from .mysql_test import DB
import time


def test():
    result=DB.execution(DB.select, "select * from test")
    return result
