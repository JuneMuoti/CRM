from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.
# convention is to use prefix "test" for each teast name
class HomePageTest(TestCase):

    def test_get(self):
        response=self.client.get(reverse("home-page"))
        print(response)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"home_page.html")
        

    
 