from gumicorn.config import Config
from gumicorn.http.errors import LimitRequestHeaders

request = LimitRequestHeaders
cfg = Config()
cfg.set('limit_request_field_size', 10)
