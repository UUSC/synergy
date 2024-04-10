mike=int(input("Количество денег у майкла:"))
ivan=int(input("Количество денег у Ивана:"))
min_vlozh=1000#int(input("минимальная сумма вложений"))
if mike>=min_vlozh and ivan>=min_vlozh:
    print("2")
elif mike>=min_vlozh and ivan<=min_vlozh:
    print("mike")
elif mike<=min_vlozh and ivan>=min_vlozh:
    print("ivan")
elif mike+ivan>=min_vlozh:
    print("1")
else:
    print("0")

# 1500
# 1500
# rez 2
# -----------
# 1500
# 500
# rez mike
# -----------
# 500
# 1500
# rez ivan
# -----------
# 500
# 500
# rez 1
# -----------
# 200
# 200
# rez 0