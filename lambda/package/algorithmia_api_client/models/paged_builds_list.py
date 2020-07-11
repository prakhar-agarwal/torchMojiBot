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


class PagedBuildsList(object):
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
        'next_link': 'str',
        'marker': 'str',
        'results': 'list[object]'
    }

    attribute_map = {
        'next_link': 'next_link',
        'marker': 'marker',
        'results': 'results'
    }

    def __init__(self, next_link=None, marker=None, results=None):  # noqa: E501
        """PagedBuildsList - a model defined in OpenAPI"""  # noqa: E501

        self._next_link = None
        self._marker = None
        self._results = None
        self.discriminator = None

        if next_link is not None:
            self.next_link = next_link
        if marker is not None:
            self.marker = marker
        if results is not None:
            self.results = results

    @property
    def next_link(self):
        """Gets the next_link of this PagedBuildsList.  # noqa: E501


        :return: The next_link of this PagedBuildsList.  # noqa: E501
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this PagedBuildsList.


        :param next_link: The next_link of this PagedBuildsList.  # noqa: E501
        :type: str
        """

        self._next_link = next_link

    @property
    def marker(self):
        """Gets the marker of this PagedBuildsList.  # noqa: E501


        :return: The marker of this PagedBuildsList.  # noqa: E501
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this PagedBuildsList.


        :param marker: The marker of this PagedBuildsList.  # noqa: E501
        :type: str
        """

        self._marker = marker

    @property
    def results(self):
        """Gets the results of this PagedBuildsList.  # noqa: E501


        :return: The results of this PagedBuildsList.  # noqa: E501
        :rtype: list[object]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PagedBuildsList.


        :param results: The results of this PagedBuildsList.  # noqa: E501
        :type: list[object]
        """

        self._results = results

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
        if not isinstance(other, PagedBuildsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
