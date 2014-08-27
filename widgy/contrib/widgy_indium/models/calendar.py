from django.utils.translation import ugettext_lazy as _
from django.db import models

from widgy.models import Content
from widgy.models.mixins import (
    StrictDefaultChildrenMixin, InvisibleMixin, StrDisplayNameMixin,
    TabbedContainer,
)

import widgy
  
from widgy.contrib.page_builder.models import CssContainerClasses

@widgy.register
class Calendar(StrDisplayNameMixin, Content, CssContainerClasses):    
    title = models.CharField(max_length=255, default="", verbose_name=_('title'), null=False, blank=False)

    calendar_url = models.CharField(_('calendar url'), help_text="Google Calendar XML-feed", max_length=500) 

    show_header = models.BooleanField(default=True, verbose_name=_("show header"))
    header_left = models.CharField(verbose_name=_("header left"), help_text="http://arshaw.com/fullcalendar/docs/display/header/", default="title", max_length=100)
    header_center = models.CharField(verbose_name=_("header center"), help_text="http://arshaw.com/fullcalendar/docs/display/header/", default="month,agendaWeek,agendaDay", max_length=100)
    header_right = models.CharField(verbose_name=_("header right"), help_text="http://arshaw.com/fullcalendar/docs/display/header/", default="today prev,next prevYear,nextYear", max_length=100)

    WEEKDAYS = (
            (0, _("Sun")), 
            (1, _("Mon")), 
            (2, _("Tue")), 
            (3, _("Wed")), 
            (4, _("Thu")), 
            (5, _("Fri")), 
            (6, _("Sat")),
    )
    first_day = models.PositiveIntegerField(default=1, verbose_name=_("first day"), choices=WEEKDAYS)
    show_week_number = models.BooleanField(default=True, verbose_name=_("show week number"))

    agenda_time_format = models.CharField(_('agenda time format'), max_length=50, help_text="http://arshaw.com/fullcalendar/docs/text/timeFormat/", default="H:mm{ - H:mm}")
    time_format = models.CharField(_('time format'), max_length=50, help_text="http://arshaw.com/fullcalendar/docs/text/timeFormat/", default="H:mm")
    column_format_month = models.CharField(_('format for month column'), max_length=50, help_text="http://arshaw.com/fullcalendar/docs/text/columnFormat/", default="ddd")
    column_format_week = models.CharField(_('format for week column'), max_length=50, help_text="http://arshaw.com/fullcalendar/docs/text/columnFormat/", default="ddd dd.MM.")
    column_format_day = models.CharField(_('format for day column'), max_length=50, help_text="http://arshaw.com/fullcalendar/docs/text/columnFormat/", default="dddd dd.MM.")

    event_background_color = models.CharField(_('event background color'), max_length=50, default="rgba(255,255,255,0.2)")
    event_border_color = models.CharField(_('event border color'), max_length=50, default="#ddd")
    event_text_color = models.CharField(_('event text color'), max_length=50, default="#333")


    draggable = True
    deletable = True
    accepting_children = False
    editable = True

    class Meta:
        verbose_name = _('calendar')
        verbose_name_plural = _('calendars')
        permissions = (
                    ("can_add_calendar_css_classes", "Can add Calendar CSS classes"),
            )
            
        app_label = "widgy_indium"

    def __str__(self):
        return self.title

@widgy.register
class CalendarEvents(Content, CssContainerClasses):    
    calendar_url = models.CharField(_('calendar url'), help_text="Google Calendar XML-feed. Please, change the 'basic' from the end to 'full'.", max_length=500) 

    event_count = models.PositiveIntegerField(default=3, verbose_name=_("event count"))

    draggable = True
    deletable = True
    accepting_children = False
    editable = True

    class Meta:
        verbose_name = _('calendar events')
        verbose_name_plural = _('calendar events')
        permissions = (
                    ("can_add_calendar_events_css_classes", "Can add Calendar Events CSS classes"),
            )
            
        app_label = "widgy_indium"

    def save(self, *args, **kw):

        if self.calendar_url.endswith("basic"):
            self.calendar_url = self.calendar_url[:len(self.calendar_url)-5] + "full"

        super(CalendarEvents, self).save(*args, **kw) 


