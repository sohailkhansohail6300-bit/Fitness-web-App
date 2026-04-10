from django.contrib.sitemaps import Sitemap
from .models import SEO

class SEOSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return SEO.objects.all()

    def location(self, obj):
        return obj.canonical_url