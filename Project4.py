store = {
    "хліб": 20.50,
    "морозиво": 121.21,
    "молоко": 45.50,
    "чипси": 40.00,
    "яблуко": 25.25,
    "сік": 30.00,
    "батон": 27.01
    }

def convert(price: float):
    return f"ціна: {price:.2f} грн"

def is_available(*products):
    products_dict = {}
    for i in products:
        products_dict[i] = i in store
    return products_dict

def order_info(order: list[str], option: str):
    price = 0.00
    if not order:
        return "Порожнє замовлення"
    else:
        for i in order:
            if not i in store:
                return "Товару немає в наявності"
            price += store[i]

        price = round(price, 2)
        if option.lower() == "купити":
            return "Ви купили: " + ", ".join(order) + ". " + convert(price)
        elif option.lower() == "переглянути ціну" or option.lower() == "ціна":
            return convert(price)
        else:
            return "Невідома опція"

def main():
    print(convert(25.45))
    print(convert(20))
    
    print(is_available("яблуко","хліб","шоколад","молоко"))
    
    print(order_info(["яблуко","молоко","морозиво","хліб"], "ціна"))
    print(order_info(["яблуко","молоко","морозво"], "Купити"))
    
    
    
if __name__=="__main__":
    main()
