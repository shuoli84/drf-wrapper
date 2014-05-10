drf-wrapper is a restful api wrapper which can bundle several api calls into one

Motivation:
When we design restful api, we tends to design clean api, one resource for one endpoints. 
When we get data from api, we tends to reduce the number of requests, so we would like to 
get all related resources with minimum api.

With drf-wrapper, you can design clean api, and call the wrapper api to get all required 
data with just one requests.

How it works:
It is very simple, parse the required api url as query string like:
http://127.0.0.1/api/wrapper/?urls=/api/item_a/,/api/item_b/

The library will carry over all the cookie, header from the orignal request to each api view,
that means all permission checking etc works the same as before.

Installation:
* pip install drf_wrapper

* in your settings add 'drf_wrapper' into app

* in urls.py
    urlpatterns += patterns(
        '',
        url(r'wrapper/', 'drf_wrapper.views.wrapper_view')
    )

Roadmap:
* Add pass through param support. Enable api calls like: /api/wrapper?urls=/api/hot_item,/api/company/{0:company_id}/
* Add threshold. The maximum apis can be bundled in one wrapper. 
