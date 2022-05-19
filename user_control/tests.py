from django.test import TestCase
from rest_framework.test import APITestCase
from .views import get_random,get_access_token,get_refresh_token
# Create your tests here.

class TestGenericFunctions(APITestCase):
    def test_get_randon(self):
        rand1 = get_random(10)
        rand2 = get_random(10)
        rand3 = get_random(15)
        ## to check if it sends any value or not
        self.assertTrue(rand1)

        # to check the equality of 2 values

        self.assertEqual(len(rand1),10)

    def test_get_access_token(self):
        payload = {
            "id":1,

        }
        token =get_access_token(payload)
        self.assertTrue(token)

    def test_get_refresh_token(self):
        
        token =get_refresh_token()
        self.assertTrue(token)