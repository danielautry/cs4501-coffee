from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from .models import CoffeeProduct

class CoffeeProductTestCases(TestCase):
    fixtures = ['db.json']
    def setUp(self):
        pass

    def testViewSpecificCoffee(self):
        responseSlot1 = self.client.get(reverse('viewCoffeeProduct', args={1}))
        self.assertContains(responseSlot1, 'Signature Roast')

    def testViewAllCoffee(self):
        response1 = self.client.get(reverse('viewCoffeeProduct', args={1}))
        response2 = self.client.get(reverse('viewCoffeeProduct', args={2}))
        response3 = self.client.get(reverse('viewCoffeeProduct', args={3}))
        response4 = self.client.get(reverse('viewCoffeeProduct', args={4}))
        response5 = self.client.get(reverse('viewCoffeeProduct', args={5}))
        self.assertContains(response1, 'Signature')
        self.assertContains(response2, 'Dark')
        self.assertContains(response3, 'French')
        self.assertContains(response4, 'Java')
        self.assertContains(response5, 'Medium')

    def testViewCoffeeDoesNotExist(self):
        response = self.client.get(reverse('viewCoffeeProduct', args={6}))
        resp_json = (response.content).decode("utf-8")
        self.assertEquals(resp_json, '{"Error": "Coffee Product does not exist"}')
        self.assertEquals(response.status_code, 200)

    def testCreateCoffee(self):
        responseCreate = self.client.post(reverse('createCoffeeProduct'), {'coffeeType' : 'Grit Roast', 'price' : '20'})
        self.assertEqual(responseCreate.status_code, 200)

    def testUpdateCoffee(self):
        self.client.post(reverse('viewCoffeeProduct', args={1}), {'newPrice' : '30'})
        responseUpdate = self.client.get(reverse('viewCoffeeProduct', args={1}))
        resp_json = (responseUpdate.content).decode("utf-8")
        self.assertContains(responseUpdate, '30')

    def testUpdateCoffeeDoesNotWork(self):
        self.client.post(reverse('viewCoffeeProduct', args={1}), {'price' : '30'})
        responseUpdate = self.client.get(reverse('viewCoffeeProduct', args={1}))
        resp_json = (responseUpdate.content).decode("utf-8")
        self.assertEquals(resp_json, '{"Error": "Coffee Product does not exist"}')

    def testDeleteCoffee(self):
        responseDelete = self.client.delete('/coffeeProduct/1/')
        self.assertEqual(responseDelete.status_code, 200)

    def tearDown(self):
        pass
