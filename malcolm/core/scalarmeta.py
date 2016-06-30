from collections import OrderedDict

from malcolm.core.serializable import Serializable


class ScalarMeta(Serializable):
    """Abstract base class for Scalar Meta objects"""

    def __init__(self, name, description, *args):
        super(ScalarMeta, self).__init__(name, *args)
        self.description = description
        self.writeable = True

    def validate(self, value):
        """
        Abstract function to validate a given value

        Args:
            value(abstract): Value to validate
        """

        raise NotImplementedError(
            "Abstract validate function must be implemented in child classes")

    def set_writeable(self, writeable, notify=True):
        self.writeable = writeable
        self.on_changed([["writeable"], writeable], notify)

    def to_dict(self):
        """Convert object attributes into a dictionary"""

        d = OrderedDict()
        d["description"] = self.description
        d["typeid"] = self.typeid

        return d
