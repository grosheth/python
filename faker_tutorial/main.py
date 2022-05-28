from unicodedata import category
from faker import Faker

fake = Faker(locale="fr_CA")

print(fake.name())
print(fake.address())
print(fake.text())

numbers = [fake.unique.random_int() for _ in range(50)]
assert len(numbers) == len(set(numbers))    # Vérifie que tout est bien unique dans la liste
print(numbers)

for _ in range(10):
    print(fake.job())
    print(fake.file_path(depth=3, category="video"))
    print(fake.credit_card_number(), fake.credit_card_expire(), fake.credit_card_security_code())
    print(fake.bothify(text="???-##-???"))

