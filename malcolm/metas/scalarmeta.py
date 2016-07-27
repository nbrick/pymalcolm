from malcolm.core.meta import Meta
from malcolm.compat import base_string


class ScalarMeta(Meta):
    """Abstract base class for Scalar Meta objects"""

    endpoints = ["description", "tags", "writeable", "label"]

    def __init__(self, description="", tags=None, writeable=False, label=None):
        super(ScalarMeta, self).__init__(description, tags)
        self.set_writeable(writeable)
        self.set_label(label)

    def validate(self, value):
        """
        Abstract function to validate a given value

        Args:
            value(abstract): Value to validate
        """
        raise NotImplementedError(
            "Abstract validate function must be implemented in child classes")

    def set_writeable(self, writeable, notify=True):
        """Set the writeable bool"""
        assert isinstance(writeable, bool), \
            "Expected writeable to be a bool, got %s" % (writeable,)
        self.set_endpoint("writeable", writeable, notify)

    def set_label(self, label, notify=True):
        """Set the label string"""
        assert label is None or isinstance(label, base_string), \
            "Expected label to be a string, got %s" % (label,)
        self.set_endpoint("label", label, notify)
