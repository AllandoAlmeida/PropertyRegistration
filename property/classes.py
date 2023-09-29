from datetime import date, timedelta
from property.exceptions import IspropertyIsNotAvailable


""" class Immobile:
    def __init__(self, dormitorios: int, area: float, endereco: str) -> None:
        self.dormitorios = dormitorios
        self.area = area
        self.endereco = endereco
        self.alugado_em = None

    def __repr__(self) -> str:
        return (
            f"Situado a {self.endereco} \n"
            f"Possui uma área {self.area} m² \n"
            f"Possui {self.dormitorios} dormitório(s)"
        )

    def alugar(self):
        if self.alugado_em:
            raise IspropertyIsNotAvailable("Imóvel não disponível")

        self.alugado_em = date.today()
        data_saida = self.alugado_em + timedelta(days=7)
        return (
            f"Imóvel alugado!\n"
            f"Check-in em {self.alugado_em.strftime('%Y-%m-%d')}, "
            f"Check-out em {data_saida.strftime('%Y-%m-%d')}!"
        )


class Apartment(Immobile):
    def __init__(
        self,
        dormitorios: int,
        area: float,
        endereco: str,
        andar: int,
    ) -> None:
        super().__init__(dormitorios, area, endereco)
        self.andar = andar
        self.alugar()

    def __repr__(self) -> str:
        representacao = super().__repr__()
        return f"Apartamento: \n" f"{representacao} \n" f"{self.andar}º andar"


class House(Immobile):
    def __init__(
        self, dormitorios: int, area: float, endereco: str, vaga: bool
    ) -> None:
        super().__init__(dormitorios, area, endereco)
        self.vaga = vaga
        self.alugar()

    def __repr__(self) -> str:
        representacao = super().__repr__()
        return f"Casa: \n" f"{representacao} \n" f"Tem Garagem ? {self.vaga}"
 """


class Immobile:
    def __init__(self, dormitorios: int, area: float, endereco: str):
        self.dormitorios = dormitorios
        self.area = area
        self.endereco = endereco
        self.alugado_em = None

    def __repr__(self) -> str:
        return (
            f"Situado a {self.endereco} \n"
            f"Possui uma área {self.area} m² \n"
            f"Possui {self.dormitorios} dormitório(s)"
        )


class Apartment(Immobile):
    def __init__(
        self,
        dormitorios: int,
        area: float,
        endereco: str,
        andar: int,
    ) -> None:
        super().__init__(dormitorios, area, endereco)
        self.andar = andar

    def __repr__(self) -> str:
        representacao = super().__repr__()
        return f"Apartamento: \n" f"{representacao} \n" f"{self.andar}º andar"


class House(Immobile):
    def __init__(
        self, dormitorios: int, area: float, endereco: str, vaga: bool
    ) -> None:
        super().__init__(dormitorios, area, endereco)
        self.vaga = vaga

    def __repr__(self) -> str:
        representacao = super().__repr__()
        return f"Casa: \n" f"{representacao} \n" f"Tem Garagem ? {self.vaga}"


def alugar(imovel: Immobile):
    if imovel.alugado_em is not None:
        raise IspropertyIsNotAvailable("imovél nao disponivel")

    imovel.alugado_em = date.today()
    data_saida = imovel.alugado_em + timedelta(days=7)
    return (
        f"Imóvel alugado!\n"
        f"Check-in em {imovel.alugado_em}, "
        f"Check-out em {data_saida}!"
    )
