chip_change_needed = []
candy_change_needed = []
cola_change_needed = []

def cannot_give_change_out_of_coins(quarters, dimes, nickels, difference):
    if (difference <= 0):
        return False
    diff = difference
    q = quarters
    d = dimes
    n = nickels
    while (diff >= 25) & (q > 0):
        diff -= 25
        q -= 1
    while (diff >= 10) & (d > 0):
        diff -= 10
        d -= 1
    while (diff >= 5) & (n > 0):
        diff -= 5
        n -= 1
    return diff > 0

for total in range(55, 300, 5):
    for q in range(0, total/25):
        for d in range(0, total/10):
            for n in range(0, total/5):
                sum = q*25 + d*10 + n*5
                chip_change = sum - 50
                candy_change = sum - 65
                cola_change = sum - 100
                if (sum > 50) & (cannot_give_change_out_of_coins(q, d, n, chip_change)):
                    chip_change_needed.append("[%02d %02d %02d]" % (q, d, n))
                if (sum > 65) & (cannot_give_change_out_of_coins(q, d, n, candy_change)):
                    candy_change_needed.append("[%02d %02d %02d]" % (q, d, n))
                if (sum > 100) & (cannot_give_change_out_of_coins(q, d, n, cola_change)):
                    cola_change_needed.append("[%02d %02d %02d]" % (q, d, n))

for item in set(chip_change_needed):
    print item
for item in set(candy_change_needed):
    print item
for item in set(cola_change_needed):
    print item
