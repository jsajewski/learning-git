
zakupy = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
        }
print("---Lista Zakupów---\n")

sum_stuff = 0
for shop, stuff in zakupy.items():
    sum_stuff += len(stuff)
    shop_name = shop.title()
    produkty = ', '.join([item.title() for item in stuff])

    if shop == "piekarnia":
        print(f"Idę do {shop_name}, kupuje tu: {produkty}\n")
    elif shop == "warzywniak":
        print(f"Idę do {shop_name} i kupije tu: {produkty}\n")

print(f"W sumie kupuję: {sum_stuff} produktów.")