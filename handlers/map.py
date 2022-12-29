from .base import BaseMarkmojiHandler
from .handlers import *

# Get all subclasses of the base handler
map = {
    cls.emoji: cls 
    for cls in BaseMarkmojiHandler.__subclasses__()
}