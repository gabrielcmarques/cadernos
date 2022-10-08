from dataclasses import dataclass, field 


@dataclass
class Perfil:
    nome: str
    idade: int
    genero: str
    trabalho: list[str]


perfil = Perfil("Gabriel", 28, "H", ["Estudante"])
print(f"{perfil}")