from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import register_setting


register_setting(
    name="FOOTER_COMPANY",
    description=_("The company name shown in the footer of page."),
    editable=True,
    default="",
)
register_setting(
    name="FOOTER_ADRESS_STREET",
    description=_("The street for address shown in the footer of page."),
    editable=True,
    default="",
)
register_setting(
    name="FOOTER_ADRESS_POSTAL_CODE_AND_CITY",
    description=_("The postal code and city for address shown in the footer of page."),
    editable=True,
    default="",
)

register_setting(
    name="FOOTER_PHONE",
    description=_("The phone number shown in the footer of page."),
    editable=True,
    default="",
)
register_setting(
    name="FOOTER_EMAIL",
    description=_("The e-mail address shown in the footer of page."),
    editable=True,
    default="",
)

register_setting(
    name="FOOTER_COMPANY_ID",
    description=_("The company id shown in the footer of page."),
    editable=True,
    default="",
)

register_setting(
    name="FOOTER_OPENING_HOURS_ROW_1",
    description=_("The opening hours are shown in the footer of page."),
    editable=True,
    default="",
)

register_setting(
    name="FOOTER_OPENING_HOURS_ROW_2",
    description=_("The opening hours are shown in the footer of page."),
    editable=True,
    default="",
)

register_setting(
    name="FOOTER_OPENING_HOURS_ROW_3",
    description=_("The opening hours are shown in the footer of page."),
    editable=True,
    default="",
)

register_setting(
    name="FOOTER_OPENING_HOURS_ROW_4",
    description=_("The opening hours are shown in the footer of page."),
    editable=True,
    default="",
)
