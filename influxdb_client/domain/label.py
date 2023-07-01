# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


class Label(object):
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
        'id': 'str',
        'org_id': 'str',
        'name': 'str',
        'properties': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'org_id': 'orgID',
        'name': 'name',
        'properties': 'properties'
    }

    def __init__(self, id=None, org_id=None, name=None, properties=None):  # noqa: E501,D401,D403
        """Label - a model defined in OpenAPI."""  # noqa: E501
        self._id = None
        self._org_id = None
        self._name = None
        self._properties = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if org_id is not None:
            self.org_id = org_id
        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties

    @property
    def id(self):
        """Get the id of this Label.

        :return: The id of this Label.
        :rtype: str
        """  # noqa: E501
        return self._id

    @id.setter
    def id(self, id):
        """Set the id of this Label.

        :param id: The id of this Label.
        :type: str
        """  # noqa: E501
        self._id = id

    @property
    def org_id(self):
        """Get the org_id of this Label.

        :return: The org_id of this Label.
        :rtype: str
        """  # noqa: E501
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Set the org_id of this Label.

        :param org_id: The org_id of this Label.
        :type: str
        """  # noqa: E501
        self._org_id = org_id

    @property
    def name(self):
        """Get the name of this Label.

        :return: The name of this Label.
        :rtype: str
        """  # noqa: E501
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of this Label.

        :param name: The name of this Label.
        :type: str
        """  # noqa: E501
        self._name = name

    @property
    def properties(self):
        """Get the properties of this Label.

        Key-value pairs associated with this label. To remove a property, send an update with an empty value (`""`) for the key.

        :return: The properties of this Label.
        :rtype: dict(str, str)
        """  # noqa: E501
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Set the properties of this Label.

        Key-value pairs associated with this label. To remove a property, send an update with an empty value (`""`) for the key.

        :param properties: The properties of this Label.
        :type: dict(str, str)
        """  # noqa: E501
        self._properties = properties

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in self.openapi_types.items():
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
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, Label):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
