# Vypište tabulku x funkce sinus(x) pro x od 0 do 2*PI s krokem 0,1.
# Výpis bude vypadat např. takto: # sin(0.0) = 0
# sin(0.1) = 0,0998

import numpy as np

for x in np.arange(0.0, 6.4, 0.1):
    print("sin(", round(x, 2), ") = ", round(np.sin(x), 4))
