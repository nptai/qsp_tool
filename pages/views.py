# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404

# Create your views here.
import json, os, random
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from shopify_auth.decorators import login_required
import shopify

from pages.forms import CreatePage
from pages.models import Page
from bsp_server.settings import STATIC_URL, PREVIEW_ROOT, SHOPIFY_THEME_PREFIX
from . import forms


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        location = save_image(request.FILES.get('file'))

        return HttpResponse(json.dumps({
            'location': STATIC_URL + location
        }))

    return HttpResponseServerError()


def save_image(image):
    if image:
        fs = FileSystemStorage()
        fname = fs.save(image.name.replace(' ', '_'), image)
        return fs.url(fname)

    return ''


def dispatch_iv(request, scope, has_textfield=True):
    iv_keys = []
    for key in request.POST.keys():
        if key.startswith('%s_type_' % scope):
            iv_keys.append(key)

    iv_keys.sort()
    ivs = []

    for key in iv_keys:
        iv = {
            'type': request.POST.get(key),
            'image': '',
            'video': '',
        }

        if has_textfield:
            iv['textfield'] = request.POST.get(key.replace('type', 'textfield'))

        if iv['type'] == '1':
            iv['image'] = save_image(request.FILES.get(key.replace('type', 'image')))
        elif iv['type'] == '2':
            iv['video'] = request.POST.get(key.replace('type', 'video'))

        ivs.append(iv)

    return json.dumps(ivs, encoding='latin1')


def dispatch_videourl(request, scope):
    urls = []
    for key in request.POST.keys():
        if key.startswith(scope):
            urls.append(request.POST.get(key))

    return json.dumps(urls, encoding='latin1')


def dispatch_request(request):
    ret = {}
    for key in CreatePage.Meta.fields:
        if key == 'body_ivs':
            ret[key] = dispatch_iv(request, 'body_iv')
        elif key == 'testimonial_ivs':
            ret[key] = dispatch_iv(request, 'testimonial_iv', False)
        elif key == 'video_urls':
            ret[key] = dispatch_videourl(request, 'video_url')
        elif key == 'shop':
            ret[key] = request.user.myshopify_domain
        elif key == 'header_title':
            ret[key] = make_unique_title(request.POST.get(key))
        else:
            ret[key] = request.POST.get(key)

    return ret


def dispatch_data(form):
    body_ivs = json.loads(form.body_ivs)
    testimonial_ivs = json.loads(form.testimonial_ivs)
    video_urls = json.loads(form.video_urls)

    return body_ivs, testimonial_ivs, video_urls


def process(request, page):
    body_ivs, testimonial_ivs, video_urls = dispatch_data(page)

    # shopify side
    shopify_html = render(request, 'shopify_template.html', {
        'page': page,
        'body_ivs': body_ivs,
        'testimonial_ivs': testimonial_ivs,
        'video_urls': video_urls
    })

    published_page = shopify.Page.create({
        'title': page.header_title,
        'body_html': shopify_html.content,
        'piublished': True,
        'template_suffix': SHOPIFY_THEME_PREFIX
    })

    page.shopify_id = published_page.id

    # server side
    server_html = render(request, 'server_template.html', {
        'page': page,
        'body_ivs': body_ivs,
        'testimonial_ivs': testimonial_ivs,
        'video_urls': video_urls
    })

    open(os.path.join(PREVIEW_ROOT, '%s_%s.html' % (page.shop, page.header_title)), 'w').write(server_html.content)
    open(os.path.join(PREVIEW_ROOT, '%s_%s.json' % (page.shop, page.header_title)), 'w').write(
        serializers.serialize('json', [page]))


def make_unique_title(header_title):
    if not header_title:
        header_title = 'template'

    while Page.objects.filter(header_title=header_title).exists():
        header_title = '{0}-{1}'.format(header_title, random.randint(0, 1000000))

    return header_title


@login_required
def page_create(request):
    with request.user.session:
        if request.method == 'POST':
            dispatched = dispatch_request(request)
            form = forms.CreatePage(dispatched, request.FILES)
            if form.is_valid():
                page = form.save(commit=False)
                page.save()
                process(request, page)

                return HttpResponseRedirect(reverse('pages:preview', args=[page.shop, page.header_title]))
            else:
                return HttpResponse("Error")
        else:
            form = forms.CreatePage()

    return render(request, 'page_create.html', {'form': form})


@login_required
def page_list(request):
    with request.user.session:
        pages = Page.objects.filter(shop=request.user.myshopify_domain)
        return render(request, 'page_list.html', {'pages': pages})


@login_required
def page_edit(request, header_title):
    with request.user.session:
        page = get_object_or_404(Page,
                                 shop=request.user.myshopify_domain,
                                 header_title=header_title)

        form = forms.CreatePage(request.POST or None, request.FILES or None, instance=page)

        if form.is_valid():
            page = form.save(commit=False)
            page.save()

        return render(request, 'page_edit.html', {'page': page})


def page_preview(request, shop, header_title):
    path = os.path.join(PREVIEW_ROOT, '%s_%s.html' % (shop, header_title))
    html = open(path, 'r').read()
    return HttpResponse(html)
