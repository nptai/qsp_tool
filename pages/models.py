# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
# from django.db import models

class Page(models.Model):
    shop = models.TextField()
    header_title = models.TextField(unique=True)
    header_logo = models.ImageField(blank=True)

    header_link_text_0 = models.ImageField(blank=True)
    header_link_text_1 = models.ImageField(blank=True)
    header_link_text_2 = models.ImageField(blank=True)

    header_link_url_0 = models.ImageField(blank=True)
    header_link_url_1 = models.ImageField(blank=True)
    header_link_url_2 = models.ImageField(blank=True)

    body_heading = models.TextField(blank=True)
    body_pr_image = models.ImageField(blank=True)
    body_bg_image = models.ImageField(blank=True)

    body_buy_button = models.CharField(max_length=1, blank=True)
    body_bb_code = models.TextField(blank=True)
    body_bb_image = models.ImageField(blank=True)
    body_bb_link = models.ImageField(blank=True)
    body_above_bb = models.TextField(blank=True)
    body_below_bb = models.TextField(blank=True)
    body_ivs = models.TextField(blank=True)

    testimonial_heading = models.TextField(blank=True)
    testimonial_slider = models.CharField(max_length=1, blank=True)
    testimonial_ivs = models.TextField(blank=True)
    video_urls = models.TextField(blank=True)

    footer_address = models.ImageField(blank=True)

    footer_link_text_0 = models.ImageField(blank=True)
    footer_link_text_1 = models.ImageField(blank=True)
    footer_link_text_2 = models.ImageField(blank=True)

    footer_link_url_0 = models.ImageField(blank=True)
    footer_link_url_1 = models.ImageField(blank=True)
    footer_link_url_2 = models.ImageField(blank=True)

    footer_color_select = models.ImageField(blank=True)
    footer_font_size = models.ImageField(blank=True)
    footer_tracking_code = models.TextField(blank=True)
    footer_facebook_title = models.ImageField(blank=True)
    footer_facebook_image = models.ImageField(blank=True)
    footer_facebook_description = models.TextField(blank=True)

    submit = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.header_title

    # def _get_unique_slug(self):
    #     slug = slugify(self.title)
    #     unique_slug = slug
    #     num = 1
    #     while Article.objects.filter(slug=unique_slug).exists():
    #         unique_slug = '{}-{}'.format(slug, num)
    #         num += 1
    #     return unique_slug
    #
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = self._get_unique_slug()
    #     super().save(*args, **kwargs)
