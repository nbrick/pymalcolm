# Make a nice namespace
from malcolm.core.attribute import Attribute  # noqa
from malcolm.core.block import Block  # noqa
from malcolm.core.controller import Controller  # noqa
from malcolm.core.clientcomms import ClientComms  # noqa
from malcolm.core.map import Map  # noqa
from malcolm.core.methodmeta import MethodMeta, method_takes, method_returns, \
    REQUIRED, OPTIONAL  # noqa
from malcolm.core.part import Part  # noqa
from malcolm.core.process import Process  # noqa
from malcolm.core.request import Request, Get, Put, Post, Subscribe, \
    Unsubscribe  # noqa
from malcolm.core.response import Response, Return, Error, Delta, Update  # noqa
from malcolm.core.serializable import Serializable, serialize_object, \
    deserialize_object  # noqa
from malcolm.core.servercomms import ServerComms  # noqa
from malcolm.core.statemachine import RunnableDeviceStateMachine, \
    DefaultStateMachine  # noqa
from malcolm.core.syncfactory import SyncFactory  # noqa
from malcolm.core.table import Table  # noqa
import vmetas  # noqa
