# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django import forms
from django.contrib.postgres.fields import ArrayField
import numpy as np


class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of choices.

    Uses Django 1.9's postgres ArrayField
    and a MultipleChoiceField for its formfield.
    """

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.MultipleChoiceField,
            'choices': self.base_field.choices,
        }
        defaults.update(kwargs)
        # Skip our parent's formfield implementation completely as we don't
        # care for it.
        # pylint:disable=bad-super-call
        return super(ArrayField, self).formfield(**defaults)


class Page(models.Model):
    shop = models.TextField()
    shopify_id = models.TextField(blank=True)

    header_title = models.TextField(unique=True, default='template')
    header_logo = models.ImageField(blank=True)

    header_link_texts = ArrayField(base_field=models.TextField(blank=True), default=list, size=3)
    # header_link_urls = ArrayField(base_field=models.URLField(blank=True), default=[], size=3, null=True)

    body_heading = models.TextField(blank=True, default='')
    body_pr_image = models.ImageField(blank=True)
    body_bg_image = models.ImageField(blank=True)

    body_buy_button = models.IntegerField(
        choices=(
            (0, 'none'),
            (1, 'code'),
            (2, 'image')
        ),
        default=0
    )
    body_bb_code = models.TextField(blank=True)
    body_bb_image = models.ImageField(blank=True)
    body_bb_link = models.URLField(blank=True)
    body_above_bb = models.TextField(blank=True)
    body_below_bb = models.TextField(blank=True)

    # body_iv_types = ArrayField(
    #     base_field=models.TextField(blank=True),
    #     default=["_"]*10,
    #     size=10,
    # )
    #
    body_iv_images = ArrayField(base_field=models.ImageField(blank=True),
                                default=['']*3, size=3)
    # body_iv_videos = ArrayField(base_field=models.URLField(blank=True), default=[], size=10, null=True)
    # body_iv_textfields = ArrayField(base_field=models.TextField(blank=True), default=[], size=10, null=True)

    # testimonial_heading = models.TextField(blank=True)
    # testimonial_slider = models.BooleanField(default=False)
    #
    # testimonial_iv_types = ArrayField(
    #     base_field=models.IntegerField(
    #         choices=(
    #             (0, 'none'),
    #             (1, 'image'),
    #             (2, 'video')
    #         ),
    #         default=0
    #     ),
    #     size=10
    # )
    # testimonial_iv_images = ArrayField(base_field=models.ImageField(blank=True), size=10)
    # testimonial_iv_videos = ArrayField(base_field=models.URLField(blank=True), size=10)
    #
    # video_urls = ArrayField(base_field=models.URLField(blank=True), size=4)
    #
    # footer_address = models.ImageField(blank=True)
    #
    # footer_link_texts = ArrayField(base_field=models.TextField(blank=True), size=3)
    # footer_link_urls = ArrayField(base_field=models.URLField(blank=True), size=3)
    #
    # footer_color_select = models.TextField(blank=True)
    # footer_font_size = models.IntegerField(default=0)
    # footer_tracking_code = models.TextField(blank=True)
    # footer_facebook_title = models.TextField(blank=True)
    # footer_facebook_image = models.ImageField(blank=True)
    # footer_facebook_description = models.TextField(blank=True)

    # submit_type = models.IntegerField(
    #     choices=(
    #         (0, 'published'),
    #         (1, 'unpublished')
    #     ),
    #     default=0
    # )


def __str__(self):
    return self.header_title
