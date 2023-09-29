from property.classes import Apartment, House, Immobile, alugar


def main():
    residencia_1 = Immobile(4, 20.5, "Rua das Flores")
    Apartment_1 = Apartment(3, 45, "Rua Sobe e Desce e nunca aparece", 2)
    house_1 = House(4, 20.5, "Rua das Rosas", True)
    house_2 = House(10, 20.5, "Rua do Girassol", False)
    alugar(residencia_1)

    alugar(Apartment_1)
    alugar(house_1)
    alugar(house_2)
    print(residencia_1)
    print(Apartment_1)
    print(house_1)
    print(house_2)


if __name__ == "__main__":
    main()
