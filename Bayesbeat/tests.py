# import os
# from django import test
#
#
# class EnvironmentTest(test.TestCase):
#     """ tests whether required environments variables for testing and running the app are provided """
#
#     def test_facebook_information(self):
#         self.assertNotEqual(
#             first=os.getenv('SOCIAL_AUTH_FACEBOOK_KEY'),
#             second=None,
#             msg='SOCIAL_AUTH_FACEBOOK_KEY not found'
#         )
#         self.assertNotEqual(
#             first=os.getenv('SOCIAL_AUTH_FACEBOOK_SECRET'),
#             second=None,
#             msg='SOCIAL_AUTH_FACEBOOK_SECRET not found'
#         )
#
#     def test_google_information(self):
#         self.assertNotEqual(
#             first=os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'),
#             second=None,
#             msg='SOCIAL_AUTH_GOOGLE_OAUTH2_KEY not found'
#         )
#         self.assertNotEqual(
#             first=os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'),
#             second=None,
#             msg='SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET not found'
#         )
#
#     def test_secret_key(self):
#         self.assertNotEqual(
#             first=os.getenv('SECRET_KEY'),
#             second=None,
#             msg='SECRET_KEY not found'
#         )
