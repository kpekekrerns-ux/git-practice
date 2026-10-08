CONFIG = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "app_db",
    },
    "server": {
        "host": "0.0.0.0",
        "port": 8000,
    },
    "api": {
        "timeout": 90,
        "version": "v2",
    },
    "payment": {
        "provider": "stripe",
        "currency": "USD",
        "enabled": True,
    },
}