# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseServerError
from urllib3.util import url
from django.views.decorators.csrf import csrf_exempt
import json, os

from pages.forms import CreatePage
from pages.models import Page
from . import forms
from bsp_server.settings import STATIC_URL


def home_page(request):
    return render(request, 'pages/home_page.html')


def page_detail(request, title):
    return HttpResponse(title)


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


def page_create(request):
    if request.method == 'POST':
        dispatched = dispatch_request(request)
        # print(json.dumps(dispatched, sort_keys=True, indent=4, separators=(',', ': ')))
        print(request.FILES)
        form = forms.CreatePage(dispatched, request.FILES)
        if form.is_valid():
            try:
                form.save(commit=True)
                page = Page.objects.filter(header_title=request.POST['header_title']).first()
                body_ivs, testimonial_ivs, video_urls = dispatch_data(page)

                rended_page = render(request, 'template.html', {
                    'page': page,
                    'body_ivs': body_ivs,
                    'testimonial_ivs': testimonial_ivs,
                    'video_urls': video_urls
                })

                open("./demo/index.html", "w").write(rended_page.content)

                return HttpResponse("Success")

            except Exception as e:
                print(e.message)
                return HttpResponse("Error abc")
        else:
            return HttpResponse("Error")
    else:
        form = forms.CreatePage()

    return render(request, 'pages/page_create.html', {'form': form})
