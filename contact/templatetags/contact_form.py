from django import template
from ..forms import ContactMessagesForm

register = template.Library()

@register.inclusion_tag("contact/forms/contact_form.html", takes_context=True)
def contact_form(context):
    request = context["request"]
    try:
        form = ContactMessagesForm()
        return {"form":form}
    except:
        return {"form": None}