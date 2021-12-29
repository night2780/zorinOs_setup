from typing import Any
from . import interfaces
from .base import (
    PASSIVE_NO_RESULT as PASSIVE_NO_RESULT,
    SQL_OK as SQL_OK,
    NEVER_SET as NEVER_SET,
    ATTR_WAS_SET as ATTR_WAS_SET,
    NO_VALUE as NO_VALUE,
    PASSIVE_NO_INITIALIZE as PASSIVE_NO_INITIALIZE,
    INIT_OK as INIT_OK,
    PASSIVE_OFF as PASSIVE_OFF
)

class InstanceState(interfaces.InspectionAttr):
    session_id: Any = ...
    key: Any = ...
    runid: Any = ...
    load_options: Any = ...
    load_path: Any = ...
    insert_order: Any = ...
    modified: bool = ...
    expired: bool = ...
    is_instance: bool = ...
    callables: Any = ...
    class_: Any = ...
    manager: Any = ...
    obj: Any = ...
    committed_state: Any = ...
    expired_attributes: Any = ...
    def __init__(self, obj, manager) -> None: ...
    @property
    def attrs(self): ...
    @property
    def transient(self): ...
    @property
    def pending(self): ...
    @property
    def deleted(self): ...
    @property
    def was_deleted(self): ...
    @property
    def persistent(self): ...
    @property
    def detached(self): ...
    @property
    def session(self): ...
    @property
    def object(self): ...
    @property
    def identity(self): ...
    @property
    def identity_key(self): ...
    @property
    def parents(self): ...
    @property
    def mapper(self): ...
    @property
    def has_identity(self) -> bool: ...
    @property
    def dict(self): ...
    def get_history(self, key, passive): ...
    def get_impl(self, key): ...
    @property
    def unmodified(self): ...
    def unmodified_intersection(self, keys): ...
    @property
    def unloaded(self): ...

class AttributeState(object):
    state: Any = ...
    key: Any = ...
    def __init__(self, state, key) -> None: ...
    @property
    def loaded_value(self): ...
    @property
    def value(self): ...
    @property
    def history(self): ...
    def load_history(self): ...

class PendingCollection(object):
    deleted_items: Any = ...
    added_items: Any = ...
    def __init__(self) -> None: ...
    def append(self, value): ...
    def remove(self, value): ...