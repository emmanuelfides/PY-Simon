import time

import requests
from fastapi import FastAPI
from web3 import Web3

bsc_pancake = FastAPI()
endpoint = "https://bsc-dataseed.binance.org"
web3 = Web3(Web3.HTTPProvider(endpoint))
factoryAddress = "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"
factoryAbi = '[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[],"name":"INIT_CODE_PAIR_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
pairAbi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

factoryContract = web3.eth.contract(abi=factoryAbi, address=factoryAddress)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'content-type': 'application/json',
    'Origin': 'https://pancakeswap.finance',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

pairAddressdump = {}
token0Dump = {}


@bsc_pancake.get("/priceChart")
async def priceChart(token0: str = "", token1: str = "", lookBack: int = 50):
    token0 = token0.lower()
    token1 = token1.lower()
    try:
        pairAddress = pairAddressdump[f"{token0}{token1}"]
    except:
        pairAddress = factoryContract.functions.getPair(
            web3.to_checksum_address(token0), web3.to_checksum_address(token1)).call()
        pairAddressdump[f"{token0}{token1}"] = pairAddress
    pairContract = web3.eth.contract(abi=pairAbi, address=pairAddress)
    try:
        token0Pair = token0Dump[pairAddress]
    except:
        token0Pair = pairContract.functions.token0().call().lower()
        token0Dump[pairAddress] = token0Pair
    flipPrice = False
    if token0Pair == token1:
        flipPrice = True
        token1 = token0
        token0 = token0Pair
    json_data = {
        'query': '\n  query pairHourDatas($pairId: String, $first: Int) {\n    pairHourDatas(first: $first, where: { pair: $pairId }, orderBy: hourStartUnix, orderDirection: desc) {\n      hourStartUnix\n      reserve0\n      reserve1\n      reserveUSD\n    }\n  }\n',
        'variables': {
            'pairId': pairAddress.lower(),
            'first': lookBack,
        },
        'operationName': 'pairHourDatas',
    }
    returnData = []
    response = requests.post('https://proxy-worker.pancake-swap.workers.dev/bsc-exchange',
                             headers=headers, json=json_data).json()['data']['pairHourDatas']

    for data in response:
        price = float(data['reserve0']) / float(data['reserve1'])
        returnData.append({
            'time': float(data['hourStartUnix']),
            'price': 1 / price if flipPrice else price,
        })
    returnData = returnData[::-1]
    return returnData


@bsc_pancake.get("/tokensInfo")
async def tokensInfo(token0: str = "", token1: str = ""):

    token0 = token0.lower()
    token1 = token1.lower()
    try:
        pairAddress = pairAddressdump[f"{token0}{token1}"]
    except:
        pairAddress = factoryContract.functions.getPair(
            Web3.to_checksum_address(token0), Web3.to_checksum_address(token1)).call()
        pairAddressdump[f"{token0}{token1}"] = pairAddress
    pairContract = web3.eth.contract(abi=pairAbi, address=pairAddress)
    try:
        token0Pair = token0Dump[pairAddress]
    except:
        token0Pair = pairContract.functions.token0().call().lower()
        token0Dump[pairAddress] = token0Pair
    if token0Pair == token1:
        token1 = token0
        token0 = token0Pair
    token0Contract = web3.eth.contract(
        abi=pairAbi, address=Web3.to_checksum_address(token0))
    token0TotalSupply = token0Contract.functions.totalSupply().call()
    token1Contract = web3.eth.contract(
        abi=pairAbi, address=Web3.to_checksum_address(token1))
    token1TotalSupply = token1Contract.functions.totalSupply().call()
    json_data = {
        'query': '\n  query pairsQuery($id: ID!) {\n    pairs(where: { id: $id }) {\n      ...pairFields\n    }\n  }\n  \n  fragment pairFields on Pair {\n  token0Price\n    token1Price\n    token0 {\n      id\n      name\n      symbol\n    decimals\n  tradeVolumeUSD\n   totalLiquidity\n    derivedUSD\n}\n    token1 {\n      id\n      name\n      symbol\n    decimals\n  tradeVolumeUSD\n   totalLiquidity\n    derivedUSD\n}\n    reserveUSD\n  }\n\n',
        'variables': {
            'id': pairAddress.lower(),
        },
        'operationName': 'pairsQuery',
    }
    response = requests.post('https://proxy-worker.pancake-swap.workers.dev/bsc-exchange',
                             headers=headers, json=json_data).json()['data']['pairs'][0]
    response = {
        response['token0']['id'].lower():
            {
                'symbol': response['token0']['symbol'],
                'name': response['token0']['name'],
                'mCap': int(token0TotalSupply / 10 ** float(response['token0']['decimals']) * float(
                    response['token0']['derivedUSD'])),
                'volume': int(float(response['token0']['tradeVolumeUSD'])),
                'tvl': int(float(response['token0']['totalLiquidity']) * float(response['token0']['derivedUSD'])),
                'price': float(response['token0']['derivedUSD'])
            },
        response['token1']['id'].lower():
            {
                'symbol': response['token1']['symbol'],
                'name': response['token1']['name'],
                'mCap': int(token1TotalSupply / 10 ** float(response['token1']['decimals']) * float(
                    response['token1']['derivedUSD'])),
                'volume': int(float(response['token1']['tradeVolumeUSD'])),
                'tvl': int(float(response['token1']['totalLiquidity']) * float(response['token1']['derivedUSD'])),
                'price': float(response['token1']['derivedUSD'])
            },
        'pairTvl': int(float(response['reserveUSD']))
    }
    return response


@bsc_pancake.get("/topTokens")
async def topTokens(count: int = 50):
    json_data = {
        'query': "\n  query topTokens($first: Int) {\n  tokens(orderBy:tradeVolumeUSD, orderDirection:desc, first:$first) { \n    id\n name\n  }\n}",
        'variables': {
            'first': count,
            'operationName': 'topTokens'
        }
    }
    response = requests.post('https://proxy-worker.pancake-swap.workers.dev/bsc-exchange',
                             headers=headers, json=json_data).json()['data']['tokens']
    response = [r['id'] for r in response]
    return response
