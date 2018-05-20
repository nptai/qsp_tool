from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
import os
from shopify import Session, ShopifyResource, Asset, Theme
from django.core.files.storage import FileSystemStorage
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

    # form = forms.CreatePage()

    return render(request, 'index.html')


def dispatch(request):
    meta = request.POST

    return meta


def save_files(dir, files):
    for f in files:
        fs = FileSystemStorage(location='/home/tainp/projects/qsp_tool/files/')
        filename = fs.save(f[0], f[1])
        print(filename, fs.url(filename))


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
    ActiveSession(request)
    try:
        theme = Theme().find(role='main')[0]
        Asset().find(Config.theme_params['templates'], theme_id=theme.id)
    except Exception as e:
        print('%s: copying template ...', e)
        copy_template()


def save_html(shop, title, html):
    folder = os.path.join('pages', shop)
    if not os.path.isdir(folder):
        os.mkdir(folder)
    filename = os.path.join(folder, '%s.html' % title)
    f = open(filename, 'w')
    print f.write(html)
    f.close()
