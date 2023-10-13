coin_dict = {}
coin_data = [{"crypto":"BTC","name":"Bitcoin"},{"crypto":"ETH","name":"Ethereum"},{"crypto":"BNB","name":"Binance"},{"crypto":"USDT","name":"Tether"}]
perp_data = [{"coin":"BTC","maxLeverage":2000},{"coin":"ETH","maxLeverage":1000},{"coin":"BNB","maxLeverage":500}]
perp_dict = {}
for v in coin_data :
    perp_dict[v['crypto']] = v['name']
print(perp_dict)
# for v in perp_data :
#     perp_dict[v['coin']] = coin_dict[v['coin']]
# print(perp_dict)
perp_rate = {}
for v in perp_data :
    perp_rate[v['coin']] = v['maxLeverage']
print(perp_rate)
