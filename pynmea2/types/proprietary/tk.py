# pylint: disable=wildcard-import,unused-wildcard-import
from decimal import Decimal

from ... import nmea
from ...nmea_utils import *


# timekeeping
class FZSTK(nmea.ProprietarySentence):
    sentence_types = {}

    def __new__(_cls, manufacturer, data):
        name = manufacturer + data[1]
        sentence_type = data[1]
        cls = _cls.sentence_types.get(name, _cls)
        return super(FZSTK, cls).__new__(cls)

    def __init__(self, manufacturer, data):
        self.sentence_type = manufacturer + data[1]
        super(FZSTK, self).__init__(manufacturer, data[2:])


class FZSTKALV(TK):
    """ Alive message
    """
    fields = (
        ("Node ID", "node_id", int),
        ("DateTime Hour", "hh", int),
        ("DateTime Minute", "mm", int),
        ("DateTime Second", "ss", int),
    )


class FZSTKLAP(TK):
    """ Lap Time
    """
    fields = (
        ("Node ID", "node_id", int),
        ("Lap count total", "lapcount", int),
        ("diff Hour", "hh", int),
        ("diff Minute", "mm", int),
        ("diff Second", "ss", int),
        ("diff subsecond", "subsec", int),
    )
