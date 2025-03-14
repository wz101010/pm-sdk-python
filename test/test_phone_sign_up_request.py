# coding: utf-8

"""
    全部  API 文档

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from PMCore.Client.models.phone_sign_up_request import PhoneSignUpRequest

class TestPhoneSignUpRequest(unittest.TestCase):
    """PhoneSignUpRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PhoneSignUpRequest:
        """Test PhoneSignUpRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PhoneSignUpRequest`
        """
        model = PhoneSignUpRequest()
        if include_optional:
            return PhoneSignUpRequest(
                phone = '0',
                phone_code = '48070',
                pwd = '012345',
                email = 'A@9LCSLv1C1ylmgd0.Y2TA5TkIRHRRA401iz1CiIy.dNTRd',
                email_code = '4807',
                nick_name = '',
                avatar = '',
                data = ''
            )
        else:
            return PhoneSignUpRequest(
                phone = '0',
                phone_code = '48070',
                pwd = '012345',
        )
        """

    def testPhoneSignUpRequest(self):
        """Test PhoneSignUpRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
