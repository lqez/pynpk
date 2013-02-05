class FailToOpenPackage(Exception):
    def __str__(self):
        return "Fail to open package."


class EntityNotFound(Exception):
    def __str__(self):
        return "Entity not found."
