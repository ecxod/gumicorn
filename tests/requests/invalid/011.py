from gumicorn.config import Config
from gumicorn.http.errors import LimitRequestHeaders

request = LimitRequestHeaders
cfg = Config()
cfg.set('limit_request_fields', 2)
