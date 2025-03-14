# coding: utf-8

"""
    全部  API 文档

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from PMCore.Client.models.geo_location_model import GeoLocationModel

class TestGeoLocationModel(unittest.TestCase):
    """GeoLocationModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeoLocationModel:
        """Test GeoLocationModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeoLocationModel`
        """
        model = GeoLocationModel()
        if include_optional:
            return GeoLocationModel(
                latitude = 1.337,
                longitude = 1.337,
                location_name = '',
                location_type = '',
                recipient_name = '',
                phone_number = '',
                email = '',
                country = '',
                state = '',
                city = '',
                district = '',
                street = '',
                zip_code = '',
                address = '',
                map_type = '',
                remark = '',
                tags = '',
                enable = True,
                show_index = 56,
                create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GeoLocationModel(
        )
        """

    def testGeoLocationModel(self):
        """Test GeoLocationModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
