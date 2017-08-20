
try:
    from less.base_settings import *
    from less.prod_settings import *
except ImportError as why:
    raise why

# if local
"""
try:
    from less.local_settings import *
except ImportError as why:
    raise why
"""