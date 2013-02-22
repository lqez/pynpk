class FailToOpenPackage(Exception):
    def __str__(self):
        return "Fail to open package."


class FailToSavePackage(Exception):
    def __str__(self):
        return "Fail to save package."


class EntityNotFound(Exception):
    def __str__(self):
        return "Entity not found."
