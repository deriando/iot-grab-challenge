# IMPORTANT
#### Due to `Flask-SQLAlchemy` not following Python 3.8.3 `DateTime` format, modifications to the library is required.

Change `$python_env\Lib\site-packages\sqlalchemy\dialects\mysql\types.py` at `line 427` and `428`

`value.microseconds` change to `value.microsecond`  
`value.seconds` change to `value.second`

## Installation

Clone the repository to a local folder
```
git clone https://github.com/deriando/iot-grab-msft-challenge.git
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries for this project.

```
pip install -r requirements.txt
```

## Usage

Simply launch the `run_web_server.bat` script on a Windows machine