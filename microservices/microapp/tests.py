from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from .models import CoffeeProduct
# Create your tests here.

class CoffeeProductTestCase(TestCase):
    fixtures = ['db.json']
    def setUp(self):
        pass

    def testViewCoffee(self):
        responseSlot1 = self.client.get(reverse('viewCoffeeProduct', args={1}))
        responseSlot2 = self.client.get(reverse('viewCoffeeProduct', args={2}))
        #checks that response contains parameter order list & implicitly
        # checks that the HTTP status code is 200
        self.assertContains(responseSlot1, 'nature Roast')
        self.assertContains(responseSlot2, 'Broast')

    def testCreateCoffee(self):
        responseCreate = self.client.post(reverse('createCoffeeProduct'), {'coffeeType' : 'Grit Roast', 'price' : '20'})
        self.assertEqual(responseCreate.status_code, 200)

    def viewCoffeeFails_invalid(self):
        response = self.client.get(reverse('viewCoffeeProduct'))
        self.assertEquals(response.status_code, 404)

    def testViewCustomer(self):
        responseSlot1 = self.client.get(reverse('viewCustomer', args={1}))
        responseSlot2 = self.client.get(reverse('viewCustomer', args={2}))
        #checks that response contains parameter order list & implicitly
        # checks that the HTTP status code is 200
        self.assertContains(responseSlot1, 'Michael')
        self.assertContains(responseSlot2, 'Jim')

    def testCreateCustomer(self):
        responseCreate = self.client.post(reverse('createCustomer'), {'name' : 'Daniel', 'email' : 'hello@hello.com', 'cardNumber' : '1234'})
        self.assertEqual(responseCreate.status_code, 200)

    def viewCustFails_invalid(self):
        response = self.client.get(reverse('viewCustomer'))
        self.assertEquals(response.status_code, 404)

    def testCreateSale(self):
        responseCreate = self.client.post(reverse('createSale'), {'salesman' : 'Guy', 'amount' : 50, 'customer' : 1, 'coffeeProduct' : 1})
        self.assertEqual(responseCreate.status_code, 200)

    def testViewSale(self):
        responseSlot1 = self.client.get(reverse('viewSale', args={2}))
        responseSlot2 = self.client.get(reverse('viewSale', args={3}))
        #checks that response contains parameter order list & implicitly
        # checks that the HTTP status code is 200
        self.assertContains(responseSlot1, '11')
        self.assertContains(responseSlot2, 'Little')

    def tearDown(self):
        pass #nothing to tear down

    # def client.post
