from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from .models import *

class ProductTestCases(TestCase):
    fixtures = ['db.json']
    def setUp(self):
        pass

    def testViewSpecificProduct(self):
        responseSlot1 = self.client.get(reverse('viewProduct', args={1}))
        self.assertContains(responseSlot1, 'Coffee')

    def testViewAllProducts(self):
        response1 = self.client.get(reverse('viewProduct', args={1}))
        response2 = self.client.get(reverse('viewProduct', args={2}))
        response3 = self.client.get(reverse('viewProduct', args={3}))
        response4 = self.client.get(reverse('viewProduct', args={4}))
        response5 = self.client.get(reverse('viewProduct', args={5}))
        self.assertContains(response1, 'Coffee')
        self.assertContains(response2, 'Bud Light')
        self.assertContains(response3, 'Gatorade')
        self.assertContains(response4, 'Guinness')
        self.assertContains(response5, 'Milk')

    def testViewProductDoesNotExist(self):
        response = self.client.get(reverse('viewProduct', args={6}))
        resp_json = (response.content).decode("utf-8")
        self.assertEquals(resp_json, '{"Error": "Product does not exist"}')
        self.assertEquals(response.status_code, 200)

    def testLogin(self):
        responseLogin = self.client.login(username = 'mscott@dm.com', password = 'test')
        self.assertEqual(responseLogin, True)

    # def testLogout(self):
    #     responseLogin = self.client.post(reverse('login'), {'email' : 'mscott@dm.com', 'password' : 'test'})
    #     responseLogout = self.client.post(reverse('logout'), {'auth' : '1'})
    #     self.assertEqual(responseCreate.status_code, 200)

    # def testCreateProduct(self):
    #     self.client.login('mscott@dm.com','test')
    #     responseCreate = self.client.post(reverse('createProduct'), {'product' : 'Keystone', 'price' : '5', 'sellerEmail' : 'mscott@dm.com'})
    #     self.assertEqual(responseCreate.status_code, 200)
    #
    # def testUpdateProduct(self):
    #     self.client.post(reverse('viewProduct', args={1}), {'price' : '30'})
    #     responseUpdate = self.client.get(reverse('viewProduct', args={1}))
    #     resp_json = (responseUpdate.content).decode("utf-8")
    #     self.assertContains(responseUpdate, '30')
    #
    # def testUpdateProductDoesNotWork(self):
    #     self.client.post(reverse('viewProduct', args={1}), {'wrongField' : '30'})
    #     responseUpdate = self.client.get(reverse('viewProduct', args={1}))
    #     resp_json = (responseUpdate.content).decode("utf-8")
    #     self.assertEquals(resp_json, '{"Error": "Product does not exist"}')
    #
    # def testDeleteProduct(self):
    #     responseDelete = self.client.delete('/product/1/')
    #     self.assertEqual(responseDelete.status_code, 200)

    def tearDown(self):
        pass
