class Config(object):
    host = '35.189.164.167'
    prefix = 'BestSalePage'

    authen_params = {
        'api_key': 'ef01dc7839bc2ee0ceaa335df688915e',
        'secret': '4b2cfee0cae314060d1cc2a9f872513e',
        'callback_url': 'https://%s/auth/install' % host,
    }

    permission_params = {
        'redirect_uri': 'https://%s/auth/connect' % host,
        'scope': ['read_products, read_collection_listings, read_themes, write_themes, write_content']
    }

    theme_params = {
        'layout': 'layout/theme.%s.liquid' % prefix,
        'templates': 'templates/page.%s.liquid' % prefix
    }
