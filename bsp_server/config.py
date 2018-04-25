class Config(object):
    secret = '8374fuwekjqhf/68&(*#42g126#1234&6813HSAasdgDI78'
    host = '35.194.183.235:8888'
    prefix = 'BestSalePage'

    authen_params = {
        'api_key': 'ef01dc7839bc2ee0ceaa335df688915e',
        'secret': '4b2cfee0cae314060d1cc2a9f872513e',
        'callback_url': 'https://%s/install' % host,
    }

    permission_params = {
        'redirect_uri': 'https://%s/connect' % host,
        'scope': ['read_products, read_collection_listings, read_themes, write_themes, write_content']
    }

    theme_params = {
        'layout': 'layout/theme.%s.liquid' % prefix,
        'templates': 'templates/page.%s.liquid' % prefix
    }