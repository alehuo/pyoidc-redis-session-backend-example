# pyoidc-redis-session-backend-example

This repository contains an example project that is used to demo the Redis-based session storage for `oic` python library.

## Installation istructions

1. Create and activate Python virtual env: `python3 -m venv env` and `source env/bin/activate`
2. Run `pip install -r requirements.txt`
3. Run `pip install -i https://test.pypi.org/simple/ pyoidc-redis-session-backend-alehuo==1.0.6` (This package is not on the main PyPi repository)
4. Set environment variables
5. Run `python3 src/app.py`

..or run `docker-compose up --build` and watch the magic happen