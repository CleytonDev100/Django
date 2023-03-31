import requests

f = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
f = f.json()
a = open("Bolsadevalores.txt", "r")


d = 0
for c in a:
    d += 1
f = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
f = f.json()
with open("Bolsadevalores.txt", "a") as arquivo:
    arquivo.write(f"Momento {f['USDBRL']['create_date']:^10}:\n")
    arquivo.write(f"{'Codigo:'} {'Codein:'} {'Nome:'} {'high: '} {'low: '} {'varbid: '} {'pctChange: '} {'bid: '} {'ask: '} {'timestamp: '}\n")
    arquivo.write(f"{f['USDBRL']['code']} {f['USDBRL']['codein']} {f['USDBRL']['name']} {f['USDBRL']['high']}"
                  f"{f['USDBRL']['low']} {f['USDBRL']['varBid']} {f['USDBRL']['pctChange']}"
                  f"{f['USDBRL']['bid']} {f['USDBRL']['ask']} {f['USDBRL']['timestamp']}\n")
    print("escrevendo")
