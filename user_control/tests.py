from django.test import TestCase
from rest_framework.test import APITestCase
from .views import get_random,get_access_token,get_refresh_token
# Create your tests here.

# class TestGenericFunctions(APITestCase):
#     def test_get_randon(self):
#         rand1 = get_random(10)
#         rand2 = get_random(10)
#         rand3 = get_random(15)
#         ## to check if it sends any value or not
#         print("Testing get random function")
#         self.assertTrue(rand1)

#         # to check the equality of 2 values

#         self.assertEqual(len(rand1),10)

#     def test_get_access_token(self):
#         payload = {
#             "id":1,

#         }
#         token =get_access_token(payload)
#         print("Testing get get_access_token function")

#         self.assertTrue(token)

#     def test_get_refresh_token(self):
        
#         token =get_refresh_token()
#         print("Testing get get_refresh_token function")
#         self.assertTrue(token)

class TestFunctions(APITestCase):
    login_url = "/user/login/"
    register_url = "/user/register/"
    refresh_url = "user/refresh/"
    def Test_Login(self):
        payload = {
            "username":"admin",
            "password":"1898"

        }
        response = self.client.post(self.login_url,data = payload)
        self.assertEqual(response.status_code,5000)

    def Test_Register(self):
        payload = {
            "username":"newadmin",
            "password":"18987374"
        }
        response = self.client.post(self.register_url,data = payload)
        self.assertEqual(response.status_code,201)
