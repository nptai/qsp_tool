from django.http import HttpResponse
from django.shortcuts import redirect, render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import requests, json, os
import shopify

from config import Config

shopify.Session.setup(**Config.authen_params)


def install(request):
  print 0
  if request.GET.get('shop'):
    shop = request.GET.get('shop')
  else:
    return render(request, 'error.html')

  session = shopify.Session(shop)
  permission_url = session.create_permission_url(**Config.permission_params)

  return redirect(permission_url)


def connect(request):
  shop = request.GET.get('shop')
  if shop is None:
    return render(request, 'error.html')

  session = shopify.Session(shop)
  token = session.request_token(request.GET)
  session = shopify.Session(shop, token)
  shopify.ShopifyResource.activate_session(session)

  copy_template()

  request.session['shop'] = shop
  request.session['token'] = token
  return render(request, 'index.html')


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
  print request.POST.items()
  return HttpResponse("Success")


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


def save_html(shop, title, html):
  folder = os.path.join('pages', shop)
  if not os.path.isdir(folder):
    os.mkdir(folder)
  filename = os.path.join(folder, '%s.html' % title)
  f = open(filename, 'w')
  print f.write(html)
  f.close()
