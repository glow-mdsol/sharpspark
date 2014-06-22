from google.appengine.ext import ndb
from google.appengine.ext.webapp.util import login_required
from models import Course
import settings

__author__ = 'vikki'
import webapp2
from webapp2_extras import jinja2


def jinja2_factory(app):
    j = jinja2.Jinja2(app)
    j.environment.globals.update({'appname': settings.APPNAME,
                                  'uri_for': webapp2.uri_for})
    return j


class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(factory=jinja2_factory)

    def render_template(self, filename, **template_values):
        self.response.write(self.jinja2.render_template(filename, **template_values))


class IndexHandler(BaseHandler):
    def get(self):
        return self.render_template('index.html')


class SchoolsHandler(BaseHandler):
    def get(self):
        return self.render_template('schools.html')


class AfterSchoolsHandler(BaseHandler):
    def get(self):
        return self.render_template('afterschools.html')


class PartiesHandler(BaseHandler):
    def get(self):
        return self.render_template('parties.html')


class ContactHandler(BaseHandler):
    def get(self):
        return self.render_template('contact.html')


class TutorHandler(BaseHandler):
    def get(self):
        return self.render_template('tutor.html')


class CalendarHandler(BaseHandler):
    def get(self):
        return self.render_template('calendar.html')


class EventsHandler(BaseHandler):
    def get(self):
        date_from = self.request.get('from')
        date_to = self.request.get('to')

    @login_required
    def post(self):
        """Add an event"""
        pass


class CoursesHandler(BaseHandler):
    def get(self):
        courses = Course.query().fetch()
        return self.render_template('_courses.html', courses=courses)


class CourseHandler(BaseHandler):
    def get(self, course_id=None):
        if course_id:
            course_key = ndb.Key(urlsafe=course_id)
            course = course_key.get()
            return self.render_template('_course.html', course=course)
        else:
            return self.render_template('_course.html')

    def post(self):
        if self.request.has_key('link'):
            ckey = ndb.Key(urlsafe=self.request.get('link'))
            course = ckey.get()
        else:
            course = Course.create()

        course.title = self.request.get('title')
        course.description = self.request.get('description')
        course.duration = int(self.request.get('duration'))
        course.available = True if self.request.get('available') == 1 else False
        course.cost = float(self.request.get('cost'))
