from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from .models import *

class CustomerTestCases(TestCase):
    fixtures = ['db.json']
    def setUp(self):
        pass

    def testViewSpecificCustomer(self):
        responseSlot1 = self.client.get(reverse('viewCustomer', args={1}))
        self.assertContains(responseSlot1, 'Michael')

    def testViewAllCustomers(self):
        response1 = self.client.get(reverse('viewCustomer', args={1}))
        response2 = self.client.get(reverse('viewCustomer', args={2}))
        response3 = self.client.get(reverse('viewCustomer', args={3}))
        self.assertContains(response1, 'Michael')
        self.assertContains(response2, 'Jim')
        self.assertContains(response3, 'Dwight')

    def testViewCustomerDoesNotExist(self):
        response = self.client.get(reverse('viewCustomer', args={4}))
        resp_json = (response.content).decode("utf-8")
        self.assertEquals(resp_json, '{"Error": "Customer does not exist"}')
        self.assertEquals(response.status_code, 200)

    def testCreateCustomer(self):
        responseCreate = self.client.post(reverse('createCustomer'), {'name' : 'Daniel', 'email' : 'hello@hello.com', 'cardNumber' : '1234', 'password' : 'test'})
        self.assertEqual(responseCreate.status_code, 200)

    def login(self):
        self.client.post(reverse('login', args={1}), {'email' : 'jh@dm.com', 'password' : 'test'})
        self.assertContains(responseUpdate.status_code, '200')

    def testDeleteCustomer(self):
        responseDelete = self.client.post(reverse('destroyCustomer', args={1}))
        self.assertEqual(responseDelete.status_code, 200)

    def tearDown(self):
        pass
