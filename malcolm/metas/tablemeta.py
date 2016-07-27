from collections import OrderedDict

from malcolm.metas.scalarmeta import ScalarMeta
from malcolm.metas.scalararraymeta import ScalarArrayMeta
from malcolm.core.serializable import Serializable
from malcolm.core.table import Table
from malcolm.compat import base_string


@Serializable.register_subclass("malcolm:core/TableMeta:1.0")
class TableMeta(ScalarMeta):

    endpoints = ["elements", "description", "tags",
                 "writeable", "label", "headings"]

    def __init__(self, description="", tags=None, writeable=False, label=None):
        super(TableMeta, self).__init__(description, tags, writeable, label)
        self.set_headings([])
        self.elements = OrderedDict()

    def set_elements(self, elements, notify=True):
        """Set the elements dict from a ScalarArrayMeta or serialized dict"""
        # Check correct type
        for name, element in elements.items():
            if isinstance(element, (dict, OrderedDict)):
                element = Serializable.from_dict(element)
                elements[name] = element
            assert isinstance(element, ScalarArrayMeta), \
                "Expected ScalarArrayMeta, got %s" % (element,)
        self.set_endpoint("elements", elements, notify)

    def set_headings(self, headings, notify=True):
        """Set the headings list"""
        assert isinstance(headings, list), \
            "Expected tags to be a list, got %s" % (headings,)
        for heading in headings:
            assert isinstance(heading, base_string), \
                "Expected heading to be string, got %s" % (heading,)
        self.set_endpoint("headings", headings, notify)

    def validate(self, value):
        if not isinstance(value, Table):
            # turn it into a table
            value = Table.from_dict(value, meta=self)
        else:
            # Check that it's using the same meta object
            assert self.to_dict() == value.meta.to_dict(), \
                "Supplied table with wrong meta type"
        # Check column lengths
        value.verify_column_lengths()
        return value
