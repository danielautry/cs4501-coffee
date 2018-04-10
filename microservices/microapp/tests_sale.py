from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from .models import CoffeeProduct

class SalesTestCases(TestCase):
    fixtures = ['db.json']
    def setUp(self):
        pass

    def testViewCart(self):
        responseSlot1 = self.client.get(reverse('viewSale', args={2}))
        self.assertContains(responseSlot1, 'Daniel')

    def testViewInvalidCart(self):
        responseSlot1 = self.client.get(reverse('viewSale', args={2000}))
        resp_json = (responseSlot1.content).decode("utf-8")
        self.assertEquals(resp_json, '{"Error": "Sale does not exist"}')

    def testViewAllSales(self):
        response1 = self.client.get(reverse('viewSale', args={1}))
        response2 = self.client.get(reverse('viewSale', args={2}))
        response3 = self.client.get(reverse('viewSale', args={3}))
        self.assertContains(response1, 'Daniel')
        self.assertContains(response2, '11')
        self.assertContains(response3, 'Jeremy')

    def testCreateSale(self):
        responseCreate = self.client.post(reverse('createSale'), {'salesman' : 'Jeremy Little', 'amount' : '50', 'name' : 'Jim Halpert', 'email' : 'jh@dm.com', 'coffeeType' : 'Dark Broast'})
        self.assertEqual(responseCreate.status_code, 200)

    def testUpdateCart(self):
        self.client.post(reverse('viewSale', args={1}), {'newAmount' : '100'})
        responseUpdate = self.client.get(reverse('viewSale', args={1}))
        resp_json = (responseUpdate.content).decode("utf-8")
        self.assertContains(responseUpdate, '100')

    def testUpdateCartInvalid(self):
        self.client.post(reverse('viewSale', args={1}), {'amount' : '100'})
        responseUpdate = self.client.get(reverse('viewSale', args={1}))
        resp_json = (responseUpdate.content).decode("utf-8")
        self.assertEquals(resp_json, '{"Error": "Sale does not exist"}')

    def testDeleteSale(self):
        responseDelete = self.client.delete('/sale/1/')
        self.assertEqual(responseDelete.status_code, 200)

    def tearDown(self):
        pass
