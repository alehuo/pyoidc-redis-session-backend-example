# pyoidc-redis-session-backend-example

This repository contains an example project that is used to demo the Redis-based session storage for `oic` python library.

You can find the session storage source code at https://github.com/alehuo/pyoidc-redis-session-backend

## Installation istructions

Before running these steps, make sure you have an OIDC provider that you can use. In this case, I recommend using Auth0 for the OIDC provider.

1. Create and activate Python virtual env: `python3 -m venv env` and `source env/bin/activate`
2. Run `pip install -r requirements.txt`
3. Run `pip install -i https://test.pypi.org/simple/ pyoidc-redis-session-backend-alehuo==1.0.7` (This package is not on the main PyPi repository)
4. Set environment variables
5. Run `python3 src/app.py`

..or run `docker-compose up --build` and watch the magic happen. Remember to set the required environment variables.

## Contribution

Contributions to this repo are welcome.

## License

This project has been licensed with MIT license.