from pytest import raises
import npk


class TestNpk(object):
    def test_open_package(self):
        pack = npk.package("testres/sample.npk", (98521, 16322, 7163, 992))
        pack.close()

    def test_open_package_fail(self):
        with raises(npk.FailToOpenPackage):
            pack = npk.package("testres/sample.npk", (0, 0, 0, 0))

    def test_iterate_entities(self):
        pack = npk.package("testres/sample.npk", (98521, 16322, 7163, 992))
        entities = pack.all()
        entities_expected = ['sample.txt', 'tea.txt', 'zip.txt', 'zipntea.txt']
        assert len(entities) == 4
        assert set(sorted([str(x) for x in entities])) == set(sorted(entities_expected))
        pack.close()

    def test_get_entity(self, tmpdir):
        pack = npk.package("testres/sample.npk", (98521, 16322, 7163, 992))
        for entity in pack.all():
            assert entity.read() == open("testres/sample.txt").read()
        pack.close()

    def test_get_entity_fail(self):
        pack = npk.package("testres/sample.npk", (98521, 16322, 7163, 992))
        with raises(npk.EntityNotFound):
            pack.get("notfound.42")
        pack.close()
