from django.forms.widgets import TextInput
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.safestring import mark_safe


class TagAutocomplete(TextInput):

	def render(self, name, value, attrs=None):
		list_view = reverse('tagging_autocomplete-list')
		if not 'class' in attrs:
			attrs.update({'class' : 'vTextField'})
		html = super(TagAutocomplete, self).render(name, value, attrs)
		js = u'<script type="text/javascript">$(function() {installTaggingAutocompleate("%s", "%s") });</script>' % (attrs['id'], list_view)
		return mark_safe("\n".join([html, js]))

	class Media:
		js_base_url = getattr(settings, 'TAGGING_AUTOCOMPLETE_JS_BASE_URL', '%s/jquery-autocomplete' % settings.MEDIA_URL)
		js = (
			'lib/jquery/jquery.min.js',
			'lib/jquery/jquery-ui.min.js',
			'%s/tagging_autocomplete.js' % js_base_url,
		)
		css = {
			'screen': ('lib/jquery/ui-lightness/jquery-ui.css',),
		}
