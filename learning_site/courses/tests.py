from django.test import TestCase
from django.utils import timezone
from .models import Course, Step
from django.core.urlresolvers import reverse
# Create your tests here.

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title = 'Python Regular Expressions',
            description = 'Learn to write regex in python'
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)


class CourseViewsTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title = 'Python Testing',
            description = 'Python tests for dummies',
        )
        self.course2 = Course.objects.create(
            title = 'New course',
            description = 'A new course',
        )
        self.step = Step.objects.create(
            title = 'Introduction to duck tests',
            description = 'Learn to write tests in duck strings',
            course = self.course,
        )

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:courselist'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course,resp.context['courses'])
        self.assertIn(self.course2,resp.context['courses'])
        self.assertTemplateUsed(resp, 'courses/course_list.html')
        self.assertContains(resp, self.course.title)