from gumicorn.http.errors import InvalidHeaderName
from gumicorn.config import Config

cfg = Config()
cfg.set("header_map", "refuse")

request = InvalidHeaderName
