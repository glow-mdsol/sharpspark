# -*- coding: utf-8 -*-
__author__ = 'glow'
from google.appengine.ext import ndb

class LinkableModel(ndb.Model):
    @property
    def link(self):
        return self.key.urlsafe()


class CourseType(LinkableModel):
    name = ndb.StringProperty()


class Course(LinkableModel):
    """A course"""
    title = ndb.StringProperty()
    duration = ndb.IntegerProperty(indexed=False)
    duration_unit = ndb.StringProperty(choices=["h", "d", "w"])
    description = ndb.TextProperty(indexed=False)
    available = ndb.BooleanProperty()
    course_type = ndb
    cost = ndb.FloatProperty()

    @classmethod
    def create(cls, **kwargs):
        entity = cls(parent=ndb.Key('Course', "Courses"), **kwargs)
        return entity


class Event(LinkableModel):
    # name of event
    title = ndb.StringProperty()
    # url of event
    url = ndb.StringProperty()
    # this is for the calendar
    event_class = ndb.StringProperty()
    # publicly visible?
    visible = ndb.BooleanProperty()
    # event created
    created = ndb.DateTimeProperty(auto_now_add=True)
    # event updated
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def create(cls, **kwargs):
        entity = cls(parent=ndb.Key('Event', "Events"), **kwargs)
        return entity

