from urllib import parse

REDIRECT_URL = 'http://localhost:5000/oauth/callback'
REDIRECT_URL_LEAGUE = 'https://register.arbiters.io/oauth/callback/league'
CLIENT_SECRET = 'aoVKiRAoajbzhtwzIMtcMqtJ7w9pJDZf'
REDIRECT_URL_COUNTER = 'https://register.arbiters.io/oauth/callback/counter'
OAUTH_URL = f'https://discord.com/api/oauth2/authorize?client_id=1140740146099138640&redirect_uri={parse.quote(REDIRECT_URL)}&response_type=code&scope=identify'
OAUTH_URL_LEAGUE = f'https://discord.com/api/oauth2/authorize?client_id=1140740146099138640&redirect_uri={parse.quote(REDIRECT_URL_LEAGUE)}&response_type=code&scope=identify'
OAUTH_URL_COUNTER = f'https://discord.com/api/oauth2/authorize?client_id=1140740146099138640&redirect_uri={parse.quote(REDIRECT_URL_COUNTER)}&response_type=code&scope=identify'