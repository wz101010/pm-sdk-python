# coding: utf-8

"""
    全部  API 文档

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from PMCore.Client.models.email_sign_up_request import EmailSignUpRequest

class TestEmailSignUpRequest(unittest.TestCase):
    """EmailSignUpRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmailSignUpRequest:
        """Test EmailSignUpRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmailSignUpRequest`
        """
        model = EmailSignUpRequest()
        if include_optional:
            return EmailSignUpRequest(
                email = '0',
                pwd = '012345',
                email_code = '4807',
                phone = '48072888001',
                phone_code = '4807',
                nick_name = '',
                avatar = '',
                data = ''
            )
        else:
            return EmailSignUpRequest(
                email = '0',
                pwd = '012345',
        )
        """

    def testEmailSignUpRequest(self):
        """Test EmailSignUpRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
