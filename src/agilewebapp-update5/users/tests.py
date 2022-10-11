from django.contrib.auth.models import User
from django.test import TestCase,Client

class ProfileTestCase(TestCase):
    def setUp(self):
        self.client=Client()
        userInfo={
            'username':'test0309',
            'password':'agile0309',
            'email':'csm2020agile@gmail.com'
        }
        self.client.force_login(User.objects.create_user(userInfo))

    def test_profile_access_ok(self):
        response=self.client.get('/profile/')
        self.assertEqual(response.status_code,200)

    def test_profile_update_ok(self):
        self.assertTrue(self.client.login)
        updateInfo={
            'username':'test39',
            'email':'csm2020agile@gmail.com'
        }
        response=self.client.post('/profile/',updateInfo)

        self.assertNotEqual(response.status_code,200)

    def test_profile_update_fail(self):
        self.assertTrue(self.client.login)
        updateInfo={
            'username':'',
            'email':'csm2020agile@gmail.com'
        }
        response=self.client.post('/profile/',updateInfo)

        self.assertEqual(response.status_code,200)