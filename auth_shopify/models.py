from __future__ import unicode_literals

from django.db import models

# Create your models here.
from shopify_auth.models import AbstractShopUser


class AuthAppShopUser(AbstractShopUser):
    pass
