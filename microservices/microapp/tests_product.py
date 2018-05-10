from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core.exceptions import *
from django.utils.datastructures import MultiValueDictKeyError
import json
from .models import *

class ProductTestCases(TestCase):
    fixtures = ['db.json']
    def setUp(self):
        pass

    def testViewSpecificProduct(self):
        responseSlot1 = self.client.get(reverse('viewProduct', args={1}))
        self.assertContains(responseSlot1, 'Apple Juice')

    # def testViewAllProducts(self):
    #     response1 = self.client.get(reverse('viewProduct', args={1}))
    #     response2 = self.client.get(reverse('viewProduct', args={2}))
    #     response3 = self.client.get(reverse('viewProduct', args={3}))
    #     response4 = self.client.get(reverse('viewProduct', args={4}))
    #     response5 = self.client.get(reverse('viewProduct', args={5}))
    #     self.assertContains(response1, 'Coffee')
    #     self.assertContains(response2, 'Bud Light')
    #     self.assertContains(response3, 'Gatorade')
    #     self.assertContains(response4, 'Guinness')
    #     self.assertContains(response5, 'Milk')
    #
    # def testViewProductDoesNotExist(self):
    #     response = self.client.get(reverse('viewProduct', args={6}))
    #     resp_json = (response.content).decode("utf-8")
    #     self.assertEquals(resp_json, '{"Error": "Product does not exist"}')
    #     self.assertEquals(response.status_code, 200)
    #
    # def testCreateProduct(self):
    #     responseLogin = self.client.post(reverse('login'), {'email' : 'mscott@dm.com', 'password' : 'test'})
    #     resp = (responseLogin.content).decode("utf-8")
    #     resp_string = resp.replace("'", "\"")
    #     resp_json = json.loads(resp_string)
    #     auth = resp_json['Authenticator']
    #     responseCreate = self.client.post(reverse('createProduct'), {'product' : 'Keystone', 'price' : '5', 'auth' : auth})
    #     self.assertEqual(responseCreate.status_code, 200)
    #
    # def testProductList(self):
    #     responseLogin = self.client.post(reverse('login'), {'email' : 'mscott@dm.com', 'password' : 'test'})
    #     resp = (responseLogin.content).decode("utf-8")
    #     resp_string = resp.replace("'", "\"")
    #     resp_json = json.loads(resp_string)
    #     auth = resp_json['Authenticator']
    #     responseCreate = self.client.post(reverse('createProduct'), {'product' : 'Keystone', 'price' : '5', 'auth' : auth})
    #     responseAllProd = self.client.get(reverse('viewAllProducts'))
    #     resp_prod = (responseAllProd.content).decode("utf-8")
    #     self.assertEqual(responseAllProd.status_code, 200)
    #
    # def testCreateProductInvalidProduct(self):
    #     responseLogin = self.client.post(reverse('login'), {'email' : 'mscott@dm.com', 'password' : 'test'})
    #     resp = (responseLogin.content).decode("utf-8")
    #     resp_string = resp.replace("'", "\"")
    #     resp_json = json.loads(resp_string)
    #     auth = resp_json['Authenticator']
    #     responseCreate = self.client.post(reverse('createProduct'), {'invalidField' : 'Keystone', 'price' : '5', 'auth' : auth})
    #     resp_prod = (responseCreate.content).decode("utf-8")
    #     self.assertEqual(resp_prod, '{"Error": "Invalid Product"}')
    #
    # def testCreateProductInvalidPrice(self):
    #     responseLogin = self.client.post(reverse('login'), {'email' : 'mscott@dm.com', 'password' : 'test'})
    #     resp = (responseLogin.content).decode("utf-8")
    #     resp_string = resp.replace("'", "\"")
    #     resp_json = json.loads(resp_string)
    #     auth = resp_json['Authenticator']
    #     responseCreate = self.client.post(reverse('createProduct'), {'product' : 'Keystone', 'invalidField' : '5', 'auth' : auth})
    #     resp_prod = (responseCreate.content).decode("utf-8")
    #     self.assertEqual(resp_prod, '{"Error": "Invalid Price"}')
    #
    # def testLogin(self):
    #     responseLogin = self.client.post(reverse('login'), {'email' : 'mscott@dm.com', 'password' : 'test'})
    #     self.assertEqual(responseLogin.status_code, 200)
    #
    # def testLoginPasswordInvalid(self):
    #     responseLogin = self.client.post(reverse('login'), {'email' : 'mscott@dm.com', 'password' : 'invalid'})
    #     resp = (responseLogin.content).decode("utf-8")
    #     self.assertEquals(resp, '{"Error": "User Invalid"}')
    #
    # def testLogout(self):
    #     responseLogin = self.client.post(reverse('login'), {'email' : 'mscott@dm.com', 'password' : 'test'})
    #     resp = (responseLogin.content).decode("utf-8")
    #     resp_string = resp.replace("'", "\"")
    #     resp_json = json.loads(resp_string)
    #     auth = resp_json['Authenticator']
    #     responseLogout = self.client.post(reverse('logout'), {'Authenticator' : auth})
    #     self.assertEqual(responseLogout.status_code, 200)
    #
    # def testUpdateProduct(self):
    #     self.client.post(reverse('viewProduct', args={1}), {'product' : 'Beer','price' : '30'})
    #     responseUpdate = self.client.get(reverse('viewProduct', args={1}))
    #     self.assertContains(responseUpdate, '30')
    #
    # def testUpdateProductField(self):
    #     self.client.post(reverse('viewProduct', args={1}), {'product' : 'Beer','price' : '20'})
    #     responseUpdate = self.client.get(reverse('viewProduct', args={1}))
    #     self.assertContains(responseUpdate, 'Beer')
    #
    # def testUpdatePriceField(self):
    #     self.client.post(reverse('viewProduct', args={1}), {'product' : 'Coffee','price' : '40'})
    #     responseUpdate = self.client.get(reverse('viewProduct', args={1}))
    #     self.assertContains(responseUpdate, '40')
    #
    # def testUpdateProductDoesNotWork(self):
    #     self.client.post(reverse('viewProduct', args={1}), {'wrongField' : '20'})
    #     responseUpdate = self.client.get(reverse('viewProduct', args={1}))
    #     resp_json = (responseUpdate.content).decode("utf-8")
    #     self.assertEquals(resp_json, '{"Error": "Product does not exist"}')
    #
    # def testDeleteProduct(self):
    #     responseDelete = self.client.post(reverse('destroyProduct', args={1}))
    #     self.assertEqual(responseDelete.status_code, 200)
    #
    # def testDeleteAllProducts(self):
    #     responseDelete1 = self.client.post(reverse('destroyProduct', args={1}))
    #     responseDelete2 = self.client.post(reverse('destroyProduct', args={2}))
    #     responseDelete3 = self.client.post(reverse('destroyProduct', args={3}))
    #     responseDelete4 = self.client.post(reverse('destroyProduct', args={4}))
    #     responseDelete5 = self.client.post(reverse('destroyProduct', args={5}))
    #     self.assertEqual(responseDelete1.status_code, 200)
    #     self.assertEqual(responseDelete2.status_code, 200)
    #     self.assertEqual(responseDelete3.status_code, 200)
    #     self.assertEqual(responseDelete4.status_code, 200)
    #     self.assertEqual(responseDelete5.status_code, 200)
    #
    # def testDeleteProductDoesNotWork(self):
    #     responseDelete = self.client.get(reverse('destroyProduct', args={1}))
    #     resp_json = (responseDelete.content).decode("utf-8")
    #     self.assertEqual(resp_json, '{"Error": "Delete Failed"}')

    def tearDown(self):
        pass
