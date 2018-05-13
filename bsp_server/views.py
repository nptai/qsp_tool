from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
import requests, json, os
from shopify import Session, ShopifyResource, Asset, Theme

from config import Config

Session.setup(**Config.authen_params)


class ActiveSession:
    def __init__(self, request):
        self.session = ShopifyResource.activate_session(
            Session(request.session['shop'], request.session['token']))

    def __del__(self):
        ShopifyResource.clear_session()


def install(request):
    if request.GET.get('shop') is None:
        return render(request, 'error.html')
    return redirect(Session(request.GET.get('shop')).create_permission_url(**Config.permission_params))


def connect(request):
    shop = request.GET.get('shop')
    if shop is None:
        return render(request, 'error.html')

    request.session['shop'] = shop
    request.session['token'] = Session(request.GET.get('shop')).request_token(request.GET)

    return render(request, 'create_page.html')


@csrf_exempt
def create_page(request):
    # session = shopify.Session(request.session['shop'], request.session['token'])
    # shopify.ShopifyResource.activate_session(session)
    #
    # shopify.Page.create({
    #     'title': request.POST.get('title'),
    #     'body_html': '<h1>Warranty</h1>\n<p><strong>Forget it</strong>, we aint giving you nothing</p>',
    #     'piublished': False,
    #     'template_suffix': Config.prefix
    # })
    jsontxt = json.dumps(request.POST.items(), sort_keys=True, indent=4, separators=(',', ': '))
    print(jsontxt)
    return HttpResponse(jsontxt)


def copy_template():
    Asset.create({
        'key': Config.theme_params['templates'],
        'value': open('./templates/page.%s.liquid' % Config.prefix).read()
    })

    Asset.create({
        'key': Config.theme_params['layout'],
        'value': open('./templates/theme.%s.liquid' % Config.prefix).read()
    })


def install_template(request):
    ActiveSession()
    try:
        theme = Theme().find(role='main')[0]
        Asset().find(Config.theme_params['templates'], theme_id=theme.id)
    except Exception as e:
        print('%s: copying template ...', e)
        copy_template();


def save_html(shop, title, html):
    folder = os.path.join('pages', shop)
    if not os.path.isdir(folder):
        os.mkdir(folder)
    filename = os.path.join(folder, '%s.html' % title)
    f = open(filename, 'w')
    print f.write(html)
    f.close()
