from django.http import HttpResponse
from django.shortcuts import redirect, render, render_to_response
from django.template import RequestContext
import requests, json
import shopify

from config import Config

shopify.Session.setup(**Config.authen_params)

def install(request):
    if request.GET.get('shop'):
        shop = request.GET.get('shop')
    else:
        return render(request, 'error.html', {})

    session = shopify.Session(shop)    
    permission_url = session.create_permission_url(**Config.permission_params)

    return redirect(permission_url)

def connect(request):  
    shop = request.GET.get('shop')
    if shop is None:
        return render(request, 'error.html', {})

    session = shopify.Session(shop)
    token = session.request_token(request.GET)
    session = shopify.Session(shop, token)
    shopify.ShopifyResource.activate_session(session)
    
    copy_template()
    
    return render(request, 'welcome.html', {})

def copy_template():
    try:
        theme = shopify.Theme().find(role='main')[0]
        shopify.Asset().find(Config.theme_params['templates'], theme_id=theme.id)
    except Exception as e:
        shopify.Asset.create({
            'key': Config.theme_params['templates'],
            'value': open('./templates/page.%s.liquid' % Config.prefix).read()
        })

        shopify.Asset.create({
            'key': Config.theme_params['layout'],
            'value': open('./templates/theme.%s.liquid' % Config.prefix).read()
        })

def create_page(published=False):
    shopify.Page.create({
        'title': 'Warranty information',
        'body_html': '<h1>Warranty</h1>\n<p><strong>Forget it</strong>, we aint giving you nothing</p>',
        'piublished': published,
        'template_suffix': Config.prefix
    })