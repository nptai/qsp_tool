class Config(object):
    secret = 'SOME_THING@secret'
    host = '40a0c916.ngrok.io'
    shopify_config = {
        'api_key': 'ef01dc7839bc2ee0ceaa335df688915e',
        'secret': '4b2cfee0cae314060d1cc2a9f872513e',
        'app_home': 'http://' + host,
        'callback_url': 'http://' + host + '/install',
        'redirect_uri': 'http://' + host + '/connect',
        'scope': ['read_products, read_collection_listings, read_themes, write_themes']
    }