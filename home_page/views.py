from django.shortcuts import render

# Create your views here.

from shopify_auth.decorators import login_required
from django.shortcuts import redirect, render
from config import Config
import shopify

shopify.Session.setup(**Config.authen_params)


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
    try:
        theme = shopify.Theme().find(role='main')[0]
        shopify.Asset().find(Config.theme_params['templates'], theme_id=theme.id)
    except Exception as e:
        print('%s: copying template ...', e)
        copy_template()


@login_required
def home(request, *args, **kwargs):
    with request.user.session:
        # install_template(request)
        return render(request, "index.html")

