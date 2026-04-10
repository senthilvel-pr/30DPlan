# inventory_checker.py

# 1. Simulating a delivery of food items
inventory_batch = [
    {"item": "Fresh Milk", "temp_c": 3, "days_to_expiry": 10},  # PASS
    {"item": "Frozen Chicken", "temp_c": -12, "days_to_expiry": 60}, # FAIL: Too warm for frozen
    {"item": "Organic Spinach", "temp_c": 4, "days_to_expiry": 1},  # WARNING: Near expiry
    {"item": "Greek Yogurt", "temp_c": 5, "days_to_expiry": 15},   # PASS
    {"item": "Raw Shrimp", "temp_c": 10, "days_to_expiry": 5},     # FAIL: Danger Zone temp
]

print("❄️  FOOD SAFETY INVENTORY AUDIT ❄️")
print("-" * 40)

for product in inventory_batch:
    name = product['item']
    temp = product['temp_c']
    expiry = product['days_to_expiry']
    
    # Validation Rules:
    # 1. Cold Chain: Most chilled food must be < 5°C. Frozen must be < -18°C.
    # 2. Shelf Life: Warning if expiry is within 2 days.
    
    if "Frozen" in name:
        if temp <= -18:
            status = "✅ PASS: Frozen chain intact."
        else:
            status = f"❌ REJECT: Temperature too high ({temp}°C)!"
    else:
        if temp <= 5:
            if expiry <= 2:
                status = "⚠️ WARNING: Temp OK, but expires soon!"
            else:
                status = "✅ PASS: Quality assured."
        else:
            status = f"❌ REJECT: Temperature Danger Zone ({temp}°C)!"

    print(f"{name:<15} | {status}")

print("-" * 40)
