from collections import OrderedDict

import unittest

from malcolm.modules.builtin.vmetas import StringArrayMeta
from malcolm.core.mapmeta import MapMeta


class TestSetters(unittest.TestCase):

    def setUp(self):
        self.mm = MapMeta("description")

    def test_values_set(self):
        self.assertIsInstance(self.mm.elements, dict)
        assert len(self.mm.elements) == 0
        assert self.mm.typeid == "malcolm:core/MapMeta:1.0"
        assert self.mm.description == "description"

    def test_set_elements(self):
        els = dict(sam=StringArrayMeta())
        self.mm.set_elements(els)
        assert self.mm.elements == els

    def test_set_required(self):
        self.test_set_elements()
        req = ("sam",)
        self.mm.set_required(req)
        assert self.mm.required == req


class TestSerialization(unittest.TestCase):

    def setUp(self):
        self.sam = StringArrayMeta()
        self.serialized = OrderedDict()
        self.serialized["typeid"] = "malcolm:core/MapMeta:1.0"
        self.serialized["elements"] = dict(c1=self.sam.to_dict())
        self.serialized["elements"]["c1"]["label"] = "C1"
        self.serialized["description"] = "desc"
        self.serialized["tags"] = ()
        self.serialized["writeable"] = False
        self.serialized["label"] = ""
        self.serialized["required"] = ("c1",)

    def test_to_dict(self):
        tm = MapMeta("desc")
        tm.set_elements(dict(c1=self.sam))
        tm.set_required(["c1"])
        assert tm.to_dict() == self.serialized

    def test_from_dict(self):
        tm = MapMeta.from_dict(self.serialized)
        assert tm.description == "desc"
        assert len(tm.elements) == 1
        expected = self.sam.to_dict()
        expected["label"] = "C1"
        assert tm.elements["c1"].to_dict() == expected
        assert tm.tags == ()
        assert tm.required == ("c1",)
