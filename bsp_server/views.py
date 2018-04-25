from django.http import HttpResponse
from django.shortcuts import redirect, render
from config import Config
import requests, json
import shopify

shopify.Session.setup(api_key=Config.shopify_config['api_key'], 
                        secret=Config.shopify_config['secret'])

def install(request):
    if request.GET.get('shop'):
        shop = request.GET.get('shop')
    else:
        return HttpResponse(response='Error:parameter shop not found', status=500)

    session = shopify.Session(shop)    
    permission_url = session.create_permission_url(scope=Config.shopify_config['scope'], 
                                redirect_uri=Config.shopify_config['redirect_uri'])

    return redirect(permission_url)

def connect(request):  
    shop = request.GET.get('shop')
    print request
    if shop is None:
        return render(request, 'error.html')

    session = shopify.Session(shop)
    token = session.request_token(request.GET)
    session = shopify.Session(shop, token)
    shopify.ShopifyResource.activate_session(session)
    copy_template()
    return render(request, 'welcome.html')

def copy_template():
    theme_id = 0
    for theme in shopify.Theme().find():
        if theme.role == 'main':
            theme_id = theme.id

    try:
        shopify.Asset().find('templates/BestSalePage.liquid', theme_id=theme_id)
    except Exception as e:
        shopify.Asset.create({
            'key': 'templates/BestSalePage.liquid',
            'value': 'omg'
        }) 
    