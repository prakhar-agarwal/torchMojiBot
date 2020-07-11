# coding: utf-8

"""
    Algorithmia Management APIs

    APIs for managing actions on the Algorithmia platform  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: support@algorithmia.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SourceControlManagementSystem(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'repository': 'str'
    }

    attribute_map = {
        'name': 'name',
        'repository': 'repository'
    }

    def __init__(self, name=None, repository=None):  # noqa: E501
        """SourceControlManagementSystem - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._repository = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if repository is not None:
            self.repository = repository

    @property
    def name(self):
        """Gets the name of this SourceControlManagementSystem.  # noqa: E501


        :return: The name of this SourceControlManagementSystem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SourceControlManagementSystem.


        :param name: The name of this SourceControlManagementSystem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def repository(self):
        """Gets the repository of this SourceControlManagementSystem.  # noqa: E501


        :return: The repository of this SourceControlManagementSystem.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this SourceControlManagementSystem.


        :param repository: The repository of this SourceControlManagementSystem.  # noqa: E501
        :type: str
        """

        self._repository = repository

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SourceControlManagementSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
