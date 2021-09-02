from django.urls import reverse, resolve
from django.test import SimpleTestCase
from User.views import UserAPIView, SingleUserAPIView, MultipleUserAPIView

class APIUrlsTests(SimpleTestCase):

    # Testing the request if its coming to "api/users" url
    def test_get_users_is_resolved(self):
        url = reverse('user_api_view')
        self.assertEquals(resolve(url).func.view_class, UserAPIView)

    # Testing the request if its coming to "api/users/<int:pk/>" url
    def test_multiple_user_is_resolved(self):
        url = reverse('multiple_user_api_view')
        self.assertEquals(resolve(url).func.view_class, MultipleUserAPIView)

    # Testing the request if its coming to "api/users/multiple" url
    def test_single_user_is_resolved(self):
        url = reverse('single_user_api_view', args=[1])
        self.assertEquals(resolve(url).func.view_class, SingleUserAPIView)