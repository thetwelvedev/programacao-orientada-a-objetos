import abc

class Tributavel(abc.ABC):

    @abc.abstractmethod
    def get_valor_imposto(self):
        """Aplica taxa de imposto sobre um determinado valor do objeto."""
        pass
