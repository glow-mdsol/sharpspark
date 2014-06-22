#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from handlers import IndexHandler, SchoolsHandler, AfterSchoolsHandler, PartiesHandler, ContactHandler, TutorHandler, \
    CalendarHandler, CourseHandler, AdminCoursesHandler, AdminCourseHandler

routes =  [
    webapp2.Route('/', IndexHandler, 'index'),
    webapp2.Route('/schools', SchoolsHandler, 'schools'),
    webapp2.Route('/afterschool', AfterSchoolsHandler, 'after_school'),
    webapp2.Route('/parties', PartiesHandler, 'parties'),
    webapp2.Route('/contact', ContactHandler, 'contact'),
    webapp2.Route('/tutor', TutorHandler, 'tutor'),
    webapp2.Route('/calendar', CalendarHandler, 'calendar'),
    webapp2.Route('/admin/courses', AdminCoursesHandler, '_courses'),
    webapp2.Route('/course/<course_id>', CourseHandler, 'course'),
    webapp2.Route('/admin/course', AdminCourseHandler, '_course_new'),
    webapp2.Route('/admin/course/<course_id>', AdminCourseHandler, '_course'),
]
app = webapp2.WSGIApplication(routes, config={}, debug=True)
