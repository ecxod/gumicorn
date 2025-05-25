from gumicorn.config import Config
from gumicorn.http.errors import InvalidSchemeHeaders

request = InvalidSchemeHeaders
cfg = Config()
cfg.set('forwarded_allow_ips', '*')
