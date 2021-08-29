import os
if(os.path.exists("binance_f/privateconfig.py")):
    from binance_f.privateconfig import *
    g_api_key = p_api_key
    g_secret_key = p_secret_key
else:
    g_api_key = "FrzEVVrMO55G9lV461jPheMeHgjEQoNuzuLEz7llQuV41r7y8VXYhiuI3wWhZlFT"
    g_secret_key = "3qwytN7WWLoshdnklikdhRdrE1Ckbu4CV9CTnwOZPWQ2q9Wz8D9rAyR5mJ89K0P3"


g_account_id = 12345678



