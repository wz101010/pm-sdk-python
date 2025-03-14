# coding: utf-8

"""
    全部  API 文档

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from PMCore.Client.api.storage_api import StorageApi


class TestStorageApi(unittest.TestCase):
    """StorageApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StorageApi()

    def tearDown(self) -> None:
        pass

    def test_storage_aggregate(self) -> None:
        """Test case for storage_aggregate

        聚合查询
        """
        pass

    def test_storage_clear(self) -> None:
        """Test case for storage_clear

        清空表数据
        """
        pass

    def test_storage_delete(self) -> None:
        """Test case for storage_delete

        删除数据
        """
        pass

    def test_storage_delete_index(self) -> None:
        """Test case for storage_delete_index

        删除索引
        """
        pass

    def test_storage_detail(self) -> None:
        """Test case for storage_detail

        数据详情
        """
        pass

    def test_storage_execute_function(self) -> None:
        """Test case for storage_execute_function

        执行函数
        """
        pass

    def test_storage_export(self) -> None:
        """Test case for storage_export

        导出数据
        """
        pass

    def test_storage_import(self) -> None:
        """Test case for storage_import

        导入数据
        """
        pass

    def test_storage_indexes(self) -> None:
        """Test case for storage_indexes

        获取索引
        """
        pass

    def test_storage_list(self) -> None:
        """Test case for storage_list

        查询数据
        """
        pass

    def test_storage_post(self) -> None:
        """Test case for storage_post

        添加数据
        """
        pass

    def test_storage_post_index(self) -> None:
        """Test case for storage_post_index

        添加索引
        """
        pass

    def test_storage_put(self) -> None:
        """Test case for storage_put

        更新数据
        """
        pass

    def test_storage_remove(self) -> None:
        """Test case for storage_remove

        删除表
        """
        pass

    def test_storage_stats(self) -> None:
        """Test case for storage_stats

        数据表统计
        """
        pass

    def test_storage_tables(self) -> None:
        """Test case for storage_tables

        获取数据表
        """
        pass


if __name__ == '__main__':
    unittest.main()
