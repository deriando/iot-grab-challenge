# IMPORTANT
#### Due to SQLAlchemy not following Python 3.8.3 DateTime format, modifications to the library is required.

Change `$python_env\Lib\site-packages\sqlalchemy\dialects\mysql\types.py` at `line 427 and 428`

`value.microseconds` change to `value.microsecond`  
`value.seconds` change to `value.second`