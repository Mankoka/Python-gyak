#készítsen python kódot, ami bekér egy egész hőmérséklet értéket
#és kiírja hogy az adott értéken milyen halmazállapotú a víz

# Bekérjük a hőmérsékletet
homerseklet = int(input("Adja meg a hőmérsékletet (°C): "))

# Meghatározzuk a víz halmazállapotát
if homerseklet <= 0:
    print("A víz szilárd halmazállapotú (jég).")
elif 0 < homerseklet < 100:
    print("A víz folyékony halmazállapotú.")
else:
    print("A víz gáz halmazállapotú (gőz).")

