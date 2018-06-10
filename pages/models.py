# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Page(models.Model):
    shop = models.TextField()
    shopify_id = models.TextField(blank=True)

    header_title = models.TextField(unique=True)
    header_logo = models.ImageField(blank=True)

    header_link_texts = ArrayField(base_field=models.TextField(blank=True), size=3)
    header_link_urls = ArrayField(base_field=models.URLField(blank=True), size=3)

    body_heading = models.TextField(blank=True)
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
    #
    # body_iv_images = ArrayField(base_field=models.ImageField(blank=True), size=10)
    # body_iv_videos = ArrayField(base_field=models.URLField(blank=True), size=10)
    # body_iv_textfields = ArrayField(base_field=models.TextField(blank=True), size=10)
    #
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

    submit_type = models.IntegerField(
        choices=(
            (0, 'published'),
            (1, 'unpublished')
        ),
        default=0
    )


def __str__(self):
    return self.header_title
