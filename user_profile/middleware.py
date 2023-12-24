from django.http import HttpResponsePermanentRedirect
from django.contrib.sites.models import Site

class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_site = Site.objects.get_current()
        current_domain = current_site.domain
        requested_host = request.get_host().partition(":")[0]
        requested_scheme = request.scheme

        if requested_host.startswith("www.") or requested_scheme == "http":
            new_url = f"https://{current_domain}{request.path}"
            return HttpResponsePermanentRedirect(new_url)
        else:
            return self.get_response(request)
