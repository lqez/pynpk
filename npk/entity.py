from ._cffi import ffi, c
from .error import *
import collections


class NpkEntity(collections.Iterator):
    def __init__(self, entity=None):
        self.entity = entity

    def __unicode__(self):
        return ffi.string(c.npk_entity_get_name(self.entity))

    def __str__(self):
        return unicode(self).encode('utf-8')

    def size(self):
        return c.npk_entity_get_size(self.entity)

    def packed_size(self):
        return c.npk_entity_get_packed_size(self.entity)

    def read(self):
        size = self.size()
        buf = ffi.new("char[]", size)
        c.npk_entity_read(self.entity, buf)
        return ffi.string(buf)

    def export(self, filename, overwrite=True):
        return c.npk_entity_export(self.entity, ffi.new("char[]", filename), overwrite)

    def next(self):
        __entity = self.entity
        if self.entity == ffi.NULL:
            raise StopIteration
        else:
            self.entity = c.npk_entity_next(self.entity)
        return NpkEntity(__entity)

    def __next__(self):
        return self.next()

    def __iter__(self):
        return self
