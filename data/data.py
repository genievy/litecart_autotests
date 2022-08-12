from dataclasses import dataclass


@dataclass
class Customer:
    company: str = None
    tax_id: int = None
    first_name: str = None
    last_name: str = None
    address_1: str = None
    address_2: str = None
    postal_code: int = None
    city: str = None
    email: str = None
    phone: str = None
    password: str = None
    captcha: str = None
