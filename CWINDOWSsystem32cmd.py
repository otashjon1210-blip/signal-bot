Microsoft Windows [Version 10.0.26100.6899]
... import pandas as pd
... import ta  # pip install ta
... import ta  # pip install taccxt
... import time... import ccxt  # pip install ccxtr ====D oldiga -100 yozilsa kerak bo'la\
...
... # ==== O'zing kiritadigan joylar ====D oldiga -100 yozilsa kerak bo'la\
...
... # ==== O'zing kiritadigan joylar ====irini tanlaEaYSdLA5xEo"          d
... BOT_TOKEN = "8311496185:AAFVn1e1Bp7H3zCTjDlvhquZEaYSdLA5xEo"... CHAT_ID = "-1003297399708"  # kanal ID oldiga -100 yozilsa kerak bo'la\i.. RSI_PERIOD = 14
... CHAT_ID = "-1003297399708"  # kanal ID oldiga -100 yozilsa kerak bdi... SYMBOL = "XAU/USD"                                                ... Sdi
... SYMBOL = "XAU/USD"
... SYMBOL = "XAU/USD"
... TIMEFRAME = "1m"  # 1m, 5m, 10m dan birini tanlage}
... TIMEFRAME = "1m"  # 1m, 5m, 10m dan birini tanla185:AAFVn1e1Bp7H3zCTjD\
... RSI_PERIOD = 14
... RSI_PERIOD = 14... # ====================================ot{8311496185:AAFVn1e1Bp7H3zCTjD\... # ====================================ot{8311496185:AAFVn1e1Bp7H3zCTjD\
......... # Telegram signal yuboruvchi funksiyabot{8311496185:AAFVn1e1Bp7H3zCTjD\... def send_telegram(message):...     url = f"https://api.telegram.org/bot{8311496185:AAFVn1e1Bp7H3zCTjD\vhquZEaYSdLA5xEo}/sendMessage"a=payload)...     payload = {"chat_id": CHAT_ID, "text": message}                   lvhquZEaYSdLA5xEo}/sendMessage"a=payload)...     payload = {"chat_id": CHAT_ID, "text": message}...     requests.post(url, data=payload)...... # CCXT orqali ma'lumot olish (OANDA yoki boshqa exchange tanlasa ham b\'ladi)change.load_markets()... exchange = ccxt.forexcom()  # forex.com dan narx olish uchun          o'ladi)change.load_markets()
... exchange = ccxt.forexcom()  # forex.com dan narx olish uchun
... exchange.load_markets()...... print("Robot ishga tushdi...")e ma'lumotini olishclose'], window=RSI_P\...... while True:o'nggi 200 ta candle ma'lumotini olish — SELL signali (RSI b...     try:...         # So'nggi 200 ta candle ma'lumotini olish...         last_rsi =...         bars = exchange.fetch_ohlcv(SYMBOL, timeframe=TIMEFRAME, limit\200) 'volume']) send_telegram(f"?? RSI {last_rsi:.2f}...         last_rsi =...         df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low'=200) 'volume']) send_telegram(f"⚠️ RSI {last_rsi:.2f}...         last_rsi =...         df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low'\se', 'volume'])                                      ...         last_rsi =...         df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=, 'close', 'volume'])                                      ...         last_rsi =...         df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=RSI_P\...                                                  ...         last_rsi = df['rsi'].iloc[-1]l shartlarif"?? RSI {last_rsi:.2f}ERIOD).rsi()...                                                  ...         last_rsi = df['rsi'].iloc[-1]l shartlarif"⚠️ RSI {last_rsi:.2f} — SELL signali (RSI b......         # Signal shartlarif"⚠️ RSI {last_rsi:.2f} — SELL signali (RSI \...         if last_rsi > 75:...             send_telegram(f"⚠️ RSI {last_rsi:.2f} — SELL signali (RSI \...         print("Xatolik:", e)                                                                          b...             send_telegram(f"?? RSI {last_rsi:.2f} — BUY signali (RSI br...         time.sleep(30)
