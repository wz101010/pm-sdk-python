# coding: utf-8

"""
    全部  API 文档

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from PMCore.Client.models.union_id_sign_in_request import UnionIDSignInRequest

class TestUnionIDSignInRequest(unittest.TestCase):
    """UnionIDSignInRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnionIDSignInRequest:
        """Test UnionIDSignInRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnionIDSignInRequest`
        """
        model = UnionIDSignInRequest()
        if include_optional:
            return UnionIDSignInRequest(
                union_id = '0',
                platform = '0',
                two_factor_code = ''
            )
        else:
            return UnionIDSignInRequest(
                union_id = '0',
                platform = '0',
        )
        """

    def testUnionIDSignInRequest(self):
        """Test UnionIDSignInRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
