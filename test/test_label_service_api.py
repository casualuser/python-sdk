# coding: utf-8

"""
    Onepanel Core

    Onepanel Core project API  # noqa: E501

    The version of the OpenAPI document: 1.0.0-beta1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import onepanel.core.api
from onepanel.core.api.api.label_service_api import LabelServiceApi  # noqa: E501
from onepanel.core.api.rest import ApiException


class TestLabelServiceApi(unittest.TestCase):
    """LabelServiceApi unit test stubs"""

    def setUp(self):
        self.api = onepanel.core.api.api.label_service_api.LabelServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_label_service_add_labels(self):
        """Test case for label_service_add_labels

        """
        pass

    def test_label_service_delete_label(self):
        """Test case for label_service_delete_label

        """
        pass

    def test_label_service_get_labels(self):
        """Test case for label_service_get_labels

        """
        pass

    def test_label_service_replace_labels(self):
        """Test case for label_service_replace_labels

        """
        pass


if __name__ == '__main__':
    unittest.main()
