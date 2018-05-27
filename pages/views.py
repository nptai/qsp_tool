# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from bsp_server.settings import PREVIEW_ROOT
import json, os

from pages.forms import CreatePage
from pages.models import Page
from . import forms
from bsp_server.settings import STATIC_URL


def home_page(request):
    return render(request, 'pages/templates/home_page.html')


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
        else:
            ret[key] = request.POST.get(key)

    return ret


def dispatch_data(form):
    body_ivs = json.loads(form.body_ivs)
    testimonial_ivs = json.loads(form.testimonial_ivs)
    video_urls = json.loads(form.video_urls)

    return body_ivs, testimonial_ivs, video_urls


def save_html(request, page):
    if page is None:
        raise Exception('cannot save page')

    body_ivs, testimonial_ivs, video_urls = dispatch_data(page)

    rended_page = render(request, 'server_template.html', {
        'page': page,
        'body_ivs': body_ivs,
        'testimonial_ivs': testimonial_ivs,
        'video_urls': video_urls
    })

    path = os.path.join(PREVIEW_ROOT, '%s.html' % request.POST.get('header_title'))
    print(path)

    open(path, 'w').write(rended_page.content)


def page_create(request):
    if request.method == 'POST':
        dispatched = dispatch_request(request)
        form = forms.CreatePage(dispatched, request.FILES)

        if form.is_valid():
            try:
                form.save(commit=True)
                page = Page.objects.filter(header_title=request.POST['header_title']).first()
                save_html(request, page)
                return HttpResponse("Success")

            except Exception as e:
                print(e.message)
                return HttpResponse(e.message)
        else:
            return HttpResponseServerError("Invalid data")
    else:
        form = forms.CreatePage()

    return render(request, 'page_create.html', {'form': form})


def page_detail(request, title):
    print(title)
    page = Page.objects.filter(header_title=title).first()
    body_ivs, testimonial_ivs, video_urls = dispatch_data(page)

    rended_page = render(request, 'server_template.html', {
        'page': page,
        'body_ivs': body_ivs,
        'testimonial_ivs': testimonial_ivs,
        'video_urls': video_urls
    })

    return rended_page
