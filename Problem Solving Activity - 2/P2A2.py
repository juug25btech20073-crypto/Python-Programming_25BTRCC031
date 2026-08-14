n = int(input("Enter number of consumers: "))

consumer_names = []
consumer_units = []
messages = []  # holds "Invalid" / "stopped" messages, in the order they occurred

# ---------- INPUT PHASE ----------
for i in range(1, n + 1):
    name = input(f"Consumer {i}: ")
    units = int(input("Units: "))

    if units == 0:
        messages.append("0 units entered. Processing stopped.")
        break

    if units < 0:
        messages.append(f"Invalid units for {name} - Skipped")
        continue

    consumer_names.append(name)
    consumer_units.append(units)

# ---------- OUTPUT PHASE ----------
# 1. Print bills for all valid consumers first
for name, units in zip(consumer_names, consumer_units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = units * 3
    elif units <= 300:
        bill = units * 5
    else:
        bill = units * 7

    print(f"{name} - {units} units - Bill: \u20b9{bill}")

# 2. Then print the skip / stop messages
for msg in messages:
    print(msg)