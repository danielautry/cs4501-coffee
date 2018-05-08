# from django.test import TestCase, Client
# from django.core.urlresolvers import reverse
#
# # Create your tests here.
# class ProductTestCases(TestCase):
#     # fixtures = ['db.json']
#     def setUp(self):
#         pass
#
#     def testCreateProduct(self):
#         responseCreate = self.client.post(reverse('createCustomer'), {'name' : 'Daniel', 'email' : 'test', 'cardNumber' : '1234', 'password' : 'test'})
#         resp_json = (responseCreate.content).decode("utf-8")
#         self.assertEqual(resp_json, 200)
#
#     def tearDown(self):
#         pass
