import os
import sys
import unittest
from collections import OrderedDict
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import setup_malcolm_paths
from mock import Mock

from malcolm.core.serializable import Serializable
from malcolm.metas.scalarmeta import ScalarMeta

# Register ScalarMeta as a sublcass of itself so we
# can instantiate it for testing purposes.
ScalarMeta.register_subclass("scalarmeta:test")(ScalarMeta)

class TestInit(unittest.TestCase):

    def setUp(self):
        self.meta = ScalarMeta("test description")

    def test_values_after_init(self):
        self.assertEqual("test description", self.meta.description)
        self.assertFalse(self.meta.writeable)


class TestValidate(unittest.TestCase):

    def setUp(self):
        self.meta = ScalarMeta("test_description")

    def test_given_validate_called_then_raise_error(self):

        expected_error_message = \
            "Abstract validate function must be implemented in child classes"

        with self.assertRaises(NotImplementedError) as error:
            self.meta.validate(1)

        self.assertEqual(expected_error_message, error.exception.args[0])


class TestUpdate(unittest.TestCase):

    def test_set_writeable(self):
        meta = ScalarMeta("test_description")
        meta.on_changed = Mock(wrap=meta.on_changed)
        writeable = True
        notify = Mock()
        meta.set_writeable(writeable, notify=notify)
        self.assertEquals(meta.writeable, writeable)
        meta.on_changed.assert_called_once_with(
            [["writeable"], writeable], notify)

    def test_set_label(self):
        meta = ScalarMeta("test_description")
        meta.on_changed = Mock(wrap=meta.on_changed)
        label = "my label"
        notify = Mock()
        meta.set_label(label, notify=notify)
        self.assertEquals(meta.label, label)
        meta.on_changed.assert_called_once_with(
            [["label"], label], notify)


class TestSerialization(unittest.TestCase):

    def setUp(self):
        self.serialized = OrderedDict()
        self.serialized["typeid"] = "filled_in_by_subclass"
        self.serialized["description"] = "desc"
        self.serialized["tags"] = []
        self.serialized["writeable"] = True
        self.serialized["label"] = "my label"

    def test_to_dict(self):
        m = ScalarMeta("desc", writeable=True, label="my label")
        m.typeid = "filled_in_by_subclass"
        self.assertEqual(m.to_dict(), self.serialized)

    def test_from_dict(self):
        @Serializable.register_subclass("filled_in_by_subclass")
        class MyScalarMeta(ScalarMeta):
            pass
        m = MyScalarMeta.from_dict(self.serialized)
        self.assertEquals(m.description, "desc")
        self.assertEquals(m.tags, [])
        self.assertEquals(m.writeable, True)
        self.assertEquals(m.label, "my label")

if __name__ == "__main__":
    unittest.main(verbosity=2)
