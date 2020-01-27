# pyoidc-redis-session-backend-example

This repository contains an example project that is used to demo the Redis-based session storage for `oic` python library.

You can find the session storage source code at https://github.com/alehuo/pyoidc-redis-session-backend

## Environment variables

Variables marked with an asterisk (`*`) needs to be set manually

- `FLASK_ENV` - Flask environment. Defaults to `production`
- `SERVER_ADDRESS` - Server address. Defaults to `http://localhost`
- `OIDC_SERVER_URL` - OpenID Connect server URL `*`
- `OIDC_CLIENT_ID` - OpenID Connect Client ID `*`
- `OIDC_CLIENT_SECRET` - OpenID Connect Client secret `*`
- `SESSION_SECRET_KEY` - Session secret key. Defaults to `unsafe`
- `SESSION_REDIS_HOST` - Redis host. Defaults to `http://redis` which points to the Redis defined in `docker-compose.yml`
- `SESSION_REDIS_POST` - Redis port. Defaults to `6379`

## Installation istructions

Before running these steps, make sure you have an OIDC provider that you can use. In this case, I recommend using Auth0 for the OIDC provider.

1. Create and activate Python virtual env: `python3 -m venv env` and `source env/bin/activate`
2. Run `pip install -r requirements.txt`
3. Set environment variables
4. Run `python3 src/app.py`

..or run `docker-compose up --build` and watch the magic happen. Remember to set the required environment variables.

## Contribution

Contributions to this repo are welcome.

## License

This project has been licensed with MIT license.