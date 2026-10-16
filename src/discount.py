def calculate_cart_total(cart_sum, tier, promos):
    price = cart_sum
    if cart_sum > 15000:
        price = cart_sum * 0.85
    for promo in promos:
        if promo == "SUMMER":
            price -= 500
        elif promo == "VIP":
            price *= 0.90
    if tier == 1:
        price *= 0.97
    elif tier == 2:
        price *= 0.93
    if price < cart_sum * 0.70:
        price = cart_sum * 0.70
    return price
