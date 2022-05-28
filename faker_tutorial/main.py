from faker import Faker

fake = Faker(locale="fr_CA")

print(fake.name())
print(fake.address())
print(fake.text())

numbers = [fake.unique.random_int() for _ in range(500)]
assert len(numbers) == len(set(numbers))

print(numbers)