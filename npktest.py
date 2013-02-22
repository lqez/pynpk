from pytest import raises
import npk


filename = "testres/sample.npk"
sample = "testres/sample.txt"
key = (98521, 16322, 7163, 992)


class TestNpk(object):
    def test_open_package(self):
        pack = npk.package(filename, key)
        pack.close()

    def test_create_package(self):
        pack = npk.package()
        pack.add(sample)
        pack.save("test.npk")
        pack.close()

    def test_open_package_fail(self):
        with raises(npk.FailToOpenPackage):
            npk.package(filename, reversed(key))

    def test_iterate_entities(self):
        pack = npk.package(filename, key)
        entities = pack.all()
        entities_expected = ['sample.txt', 'tea.txt', 'zip.txt', 'zipntea.txt']
        assert len(entities) == 4
        assert set(sorted([str(x) for x in entities])) == set(sorted(entities_expected))
        pack.close()

    def test_get_entity(self):
        pack = npk.package(filename, key)
        for entity in pack.all():
            assert entity.read() == open(sample).read()
        pack.close()

    def test_export_entity(self, tmpdir):
        pack = npk.package(filename, key)
        for entity in pack.all():
            export_filename = str(tmpdir.join(entity.name()))
            entity.export(export_filename)
            assert open(export_filename).read() == open(sample).read()
        pack.close()

    def test_get_entity_fail(self):
        pack = npk.package(filename, key)
        with raises(npk.EntityNotFound):
            pack.get("notfound.42")
        pack.close()
