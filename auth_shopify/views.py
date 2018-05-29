from django.shortcuts import render

# Create your views here.

from shopify_auth.decorators import login_required
from django.shortcuts import redirect, render
from config import Config
import shopify

shopify.Session.setup(**Config.authen_params)


def install(request):
    if request.GET.get('shop') is None:
        return render(request, 'error.html')
    return redirect(shopify.Session(request.GET.get('shop')).create_permission_url(**Config.permission_params))


def connect(request):
    shop = request.GET.get('shop')
    if shop is None:
        return render(request, 'error.html')

    request.session['shop'] = shop
    request.session['token'] = shopify.Session(request.GET.get('shop')).request_token(request.GET)

    install_template(request)
    return render(request, 'welcome.html')


def copy_template():
    shopify.Asset.create({
        'key': Config.theme_params['templates'],
        'value': open('assets/templates/page.%s.liquid' % Config.prefix).read()
    })

    shopify.Asset.create({
        'key': Config.theme_params['layout'],
        'value': open('assets/templates/theme.%s.liquid' % Config.prefix).read()
    })


def install_template(request):
    session = shopify.Session(request.session['shop'], request.session['token'])
    shopify.ShopifyResource.activate_session(session)

    try:
        theme = shopify.Theme().find(role='main')[0]
        shopify.Asset().find(Config.theme_params['templates'], theme_id=theme.id)
    except Exception as e:
        print('%s: copying template ...', e)
        copy_template()


@login_required
def home(request, *args, **kwargs):
    return render(request, "index.html")
