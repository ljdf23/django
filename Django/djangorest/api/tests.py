from django.test import TestCase
from .models import BucketList
from django.core.urlresolvers import reverse

# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        self.buscketlist_name = "Write world class mode"
        self.buscketlist = BucketList(name=self.buscketlist_name)

    def test_model_can_create_a_bucketlist(self):
        old_count = BucketList.objects.count()
        self.buscketlist.save()
        new_count = BucketList.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.client = APIClient()
        self.bucketlist_data = {'name': 'go to ibiza'}
        self.response = self.client.post(
            rever('create'),
            self.bucketlist_data,
            format="json"
        )

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability"""
        self.asserEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        change_bucketlist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)