from ._cffi import ffi, c
from .error import *
from .entity import *


class NpkPackage(object):
    def __init__(self, filename=None, teakey=(0, 0, 0, 0)):
        self.package = None
        if filename:
            self.open(filename, teakey)

    def open(self, filename, teakey=(0, 0, 0, 0)):
        try:
            self.package = c.npk_package_open(ffi.new("char[]", filename), ffi.new("int[4]", teakey))
            if self.package == ffi.NULL:
                raise FailToOpenPackage
        except:
            raise FailToOpenPackage

    def close(self):
        c.npk_package_close(self.package)

    def add(self, filename, entityname=None):
        if entityname is None:
            entityname = filename
        entity = ffi.new("void*")
        c.npk_package_add_file(self.package, ffi.new("char[]", filename), ffi.new("char[]", entityname), entity)
        return NpkEntity(entity)

    def get(self, entityname):
        entity = c.npk_package_get_entity(
            self.package,
            ffi.new("char[]", entityname)
        )
        if entity == ffi.NULL:
            raise EntityNotFound
        return NpkEntity(entity)

    def export(self, entityname, filename=None, overwrite=True):
        try:
            entity = self.get(entityname)
        except:
            raise
        return c.npk_entity_export(entity, ffi.new("char[]", filename), overwrite)

    def first(self):
        return NpkEntity(c.npk_package_get_first_entity(self.package))

    def all(self):
        return list(self.first())

    def __iter__(self):
        return self.first()
