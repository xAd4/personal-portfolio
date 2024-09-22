from django import template
from ..forms import ContactMessagesForm

register = template.Library()

@register.inclusion_tag("contact/forms/contact_form.html", takes_context=True)
def contact_form(context):
    request = context["request"]
    if request.user.is_authenticated:
        form = ContactMessagesForm()
        return {"form":form}
    else:
        return {"form": None}