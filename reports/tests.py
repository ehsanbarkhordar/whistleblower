from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Report
from .serializers import ReportSerializer


# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_report(reporter_name="", title="", description="", phone_number=""):
        if reporter_name != "" and title != "":
            Report.objects.create(reporter_name=reporter_name, title=title, description=description,
                                  phone_number=phone_number)

    def setUp(self):
        # add test data
        self.create_report("Ehsan", "Corruption in the judiciary",
                           "persuade (someone) to act in one's favor,"
                           " typically illegally or dishonestly, by a "
                           "gift of money or other inducement."
                           )
        self.create_report("Ali mohammady", "فساد", "توضیحات فارسی", "+989158762323")
        self.create_report("Noname", "The officer bribed me", "😍🤩🤷‍♂️✊😊😶😁😁😦😯😑🤣🙄🤬😮😠😠🙌🙌😚✊🤷‍♂️")
        self.create_report("Hamid", "Hahahahahhaha", "یک گزارش مفصل\n"
                                                     "بسم الله الرحمن الرحیم", "09300520717")


class GetAllReportsTest(BaseViewTest):

    def test_get_all_reports(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("reports-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Report.objects.all()
        serialized = ReportSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
