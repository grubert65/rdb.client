import ABC
from driver.interface import get_driver

def get_client(driver: str, **params):
    return get_driver(
        module="rdb.client",
        driver=driver,
        class_name="Sql",
        **params)

class Sql(ABC):

    @abstractmethod
    def select_as_dict():
        pass

    @abstractmethod
    def select_as_namedtuple():
        pass

    @abstractmethod
    def add():
        pass

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def update_on_conflict():
        pass

    @abstractmethod
    def delete():
        pass
