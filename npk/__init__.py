import collections
from cffi import FFI


ffi = FFI()
ffi.cdef(open('npk/npk.h').read())
c = ffi.dlopen('/usr/local/lib/libnpk.dylib')


class FailToOpenPackage(Exception):
    def __str__(self):
        return "Fail to open package."


class EntityNotFound(Exception):
    def __str__(self):
        return "Entity not found."


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

package = NpkPackage
entity = NpkEntity
