from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView

from sheerlike.views.generic import SheerTemplateView


urlpatterns = [
    url(r'^$', SheerTemplateView.as_view(), name='home'),
    
    url(r'^blog/', include([
        url(r'^$', TemplateView.as_view(template_name='blog/index.html'),
                   name='index'), 
        url(r'^(?P<doc_id>[\w-]+)/$',
                   SheerTemplateView.as_view(doc_type='posts',
                                           local_name='post',
                                           default_template='blog/_single.html',),
                   name='detail'),], namespace='blog')),

    url(r'^newsroom/', include([
        url(r'^$', TemplateView.as_view(template_name='newsroom/index.html'),
                   name='index'), 
        url(r'^press-resources/$',
            TemplateView.as_view(template_name='newsroom/press-resources/index.html'),
            name='press-resources'),
        url(r'^(?P<doc_id>[\w-]+)/$',
                   SheerTemplateView.as_view(doc_type='newsroom',
                                           local_name='newsroom',
                                           default_template='newsroom/_single.html',),
                   name='detail'),], namespace='newsroom')),

    url(r'^budget/',include([
        url(r'^$', TemplateView.as_view(template_name='budget/index.html'), name='home'),
        url(r'^(?P<page_slug>[\w-]+)/$',
            SheerTemplateView.as_view(),
            name='page'), 
        ], namespace="budget")),

    url(r'^the-bureau/', include([
        url(r'^$', SheerTemplateView.as_view(template_name='the-bureau/index.html'),
            name='index'),
        url(r'^(?P<page_slug>[\w-]+)/$',
            SheerTemplateView.as_view(),
            name='page'),
            ], namespace='the-bureau')),

    url(r'^doing-business-with-us/', include([
        url(r'^$',
            TemplateView.as_view(template_name='doing-business-with-us/index.html'),
            name='index'),
        url(r'^(?P<page_slug>[\w-]+)/$',
            SheerTemplateView.as_view(),
            name='page'),

    ], namespace='business')),

    url(r'^contact-us/', include([
        url(r'^$',
            TemplateView.as_view(template_name='contact-us/index.html'),
            name='index'),

    ], namespace='contact-us')),

    url(r'^events/', include([
        url(r'^$', TemplateView.as_view(template_name='events/index.html'),
            name='events'),
        url(r'^(?P<doc_id>[\w-]+)/$',
                   SheerTemplateView.as_view(doc_type='events',
                                           local_name='event',
                                           default_template='events/_single.html',),name='event_archive')
    ])),

    url(r'^offices/', include([
        url(r'^(?P<doc_id>[\w-]+)/$',
                   SheerTemplateView.as_view(doc_type='office',
                                           local_name='office',
                                           default_template='offices/_single.html',),name='detail')
    ], namespace='offices')),

    url(r'^sub-pages/', include([
        url(r'^(?P<doc_id>[\w-]+)/$',
                   SheerTemplateView.as_view(doc_type='sub_page',
                                           local_name='sub_page',
                                           default_template='sub-pages/_single.html',),name='detail')
    ], namespace='sub_page')),
    url(r'^activity-log/$', TemplateView.as_view(template_name='activity-log/index.html'), name='activity-log'),
]

from sheerlike import register_permalink

register_permalink('posts', 'blog:detail')
register_permalink('newsroom', 'newsroom:detail')
register_permalink('office', 'offices:detail')
register_permalink('sub_page', 'sub_page:detail')
register_permalink('events', 'event_archive')
