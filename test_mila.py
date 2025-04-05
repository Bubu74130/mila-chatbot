import json

# Charger le fichier JSON
with open("support_mila.json", "r") as file:
    data = json.load(file)

# Vérifier les produits
print("✅ Products available:")
for product in data["products"]:
    print(f"- {product}")

# Vérifier un produit en détail (ex: Puravive)
product_name = "Puravive"
print(f"\n🔍 Details for {product_name}:")
print(json.dumps(data["products"][product_name], indent=4))

# Vérifier les stratégies de vente
print("\n📢 Sales strategies:")
print(json.dumps(data["sales_tactics"], indent=4))

