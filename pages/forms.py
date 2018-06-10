from django import forms
from . import models


class CreatePage(forms.ModelForm):
    class Meta:
        model = models.Page

        fields = ['header_title',
                  'header_logo',
                  'header_link_text_0',
                  'header_link_text_1',
                  'header_link_text_2',
                  'header_link_url_0',
                  'header_link_url_1',
                  'header_link_url_2',
                  'body_heading',
                  'body_pr_image',
                  'body_bg_image',
                  'body_buy_button',
                  'body_bb_code',
                  'body_bb_image',
                  'body_bb_link',
                  'body_above_bb',
                  'body_below_bb',
                  'body_ivs',
                  'testimonial_heading',
                  'testimonial_slider',
                  'testimonial_ivs',
                  'video_urls',
                  'footer_address',
                  'footer_link_text_0',
                  'footer_link_text_1',
                  'footer_link_text_2',
                  'footer_link_url_0',
                  'footer_link_url_1',
                  'footer_link_url_2',
                  'footer_color_select',
                  'footer_font_size',
                  'footer_tracking_code',
                  'footer_facebook_title',
                  'footer_facebook_image',
                  'footer_facebook_description',
                  'shop',
                  ]
