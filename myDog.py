import dog

my_first_dog = dog. Kutya("Ricky", 8, 'keverék')
my_dog = dog.Kutya("Pici", 9, 'keverék')
your_dog = dog. Kutya("Rocky", 9, 'tacskó')

print(
    f"A kutyám neve: {my_dog.nev}, fajtája: {my_dog.fajta}, kora: {my_dog.kor} év, ami emberi években számolva: {my_dog.emberi_evekben()} évet jelent.")
print(
    f"A kutyád neve: {your_dog.nev}, fajtája: {your_dog.fajta}, kora: {your_dog.kor} év, ami emberi években számolva: {your_dog.emberi_evekben()} évet jelent.")
print(
    f"Az első kutyám neve: {my_first_dog.nev}, fajtája: {my_first_dog.fajta}, kora: {my_first_dog.kor} év, ami emberi években számolva: {my_first_dog.emberi_evekben()} évet jelent.")

