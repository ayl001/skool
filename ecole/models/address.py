# -*- coding: utf-8 -*-

"""
Classe Address
"""

from dataclasses import dataclass


@dataclass
class Address:
    """Adresse d'une personne (enseignant ou élève)."""
    street: str
    city: str
    postal_code: int

    def __str__(self) -> str:
        return f"{self.street}, {self.postal_code} {self.city}"
