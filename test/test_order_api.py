# coding: utf-8

"""
    全部  API 文档

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from PMCore.Client.api.order_api import OrderApi


class TestOrderApi(unittest.TestCase):
    """OrderApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrderApi()

    def tearDown(self) -> None:
        pass

    def test_order(self) -> None:
        """Test case for order

        订单详情
        """
        pass

    def test_order_create(self) -> None:
        """Test case for order_create

        创建订单
        """
        pass

    def test_orders(self) -> None:
        """Test case for orders

        订单列表
        """
        pass


if __name__ == '__main__':
    unittest.main()
