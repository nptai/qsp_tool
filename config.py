
class Config(object):
    SECRET_KEY = "SOME_THING@secret"
    HOST = "cb7876a9.ngrok.io"

    SHOPIFY_CONFIG = {
        'API_KEY': 'ef01dc7839bc2ee0ceaa335df688915e',
        'API_SECRET': '4b2cfee0cae314060d1cc2a9f872513e',
        'APP_HOME': 'http://' + HOST,
        'CALLBACK_URL': 'http://' + HOST + '/install',
        'REDIRECT_URI': 'http://' + HOST + '/connect',
        'SCOPE': 'read_products, read_collection_listings'
    }