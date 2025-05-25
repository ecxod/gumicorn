from gumicorn.config import Config
from gumicorn.http.errors import InvalidProxyLine

cfg = Config()
cfg.set("proxy_protocol", True)

request = InvalidProxyLine
