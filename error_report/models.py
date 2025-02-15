from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from django.utils import version

from error_report.settings import ERROR_DETAIL_SETTINGS

if version.get_complete_version() < (1, 10):
    from django.core.urlresolvers import reverse
else:
    from django.urls import reverse


class Error(models.Model):
    """
    Model for storing the individual errors.
    """
    kind = models.CharField(_('type'),
                            null=True, blank=True, max_length=128, db_index=True
                            )
    info = models.TextField(
        null=False,
    )
    data = models.TextField(
        blank=True, null=True
    )
    path = models.URLField(
        null=True, blank=True,
    )
    when = models.DateTimeField(
        null=False, auto_now_add=True, db_index=True,
    )
    html = models.TextField(
        null=True, blank=True,
    )
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta information for the model.
        """
        verbose_name = _('Error')
        verbose_name_plural = _('Errors')

    def __unicode__(self):
        """
        String representation of the object.
        """
        return "%s: %s" % (self.kind, self.info)

    def html_iframe(self):
        """
        Return an Iframe for Viewing Error detail in django admin
        :return:
        """
        return \
            format_html('<iframe style="width: 100%; height: {}px;" src="{}"></iframe>',
                        ERROR_DETAIL_SETTINGS.get('ERROR_DETAIL_HEIGHT', 1000),
                        reverse('error-html-link', kwargs={'error': self.id}))
