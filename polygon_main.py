import time

import requests
from fastapi import FastAPI
from web3 import Web3
from datetime import datetime, timedelta

polygon_quickswap = FastAPI()
endpoint = "https://polygon-rpc.com/"
web3 = Web3(Web3.HTTPProvider(endpoint))
factoryAddress = "0x5757371414417b8C6CAad45bAeF941aBc7d3Ab32"
factoryAbi = '[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[],"name":"INIT_CODE_PAIR_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
pairAbi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
factoryContract = web3.eth.contract(abi=factoryAbi, address=factoryAddress)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'content-type': 'application/json',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

headerss = {
    "Content-Type": "application/json",
    "X-API-KEY": "BQYUv333aLHXBM5cKxRQklczyDJt7t9Z"
}

@polygon_quickswap.get("/priceChart")
async def priceChart(token0: str = "", token1: str = "", lookBack: int = 50):
    token0 = token0.lower()
    token1 = token1.lower()

    def calculate_date(lookBack):
        current_date = datetime.now().strftime('%Y-%m-%d')

        if lookBack == 24:
            return current_date
        elif lookBack == 168:
            return (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        elif lookBack == 720:
            return (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        else:
            # Handle other cases or provide a default date
            return current_date
    date = calculate_date(lookBack)

    json_data = {
        'query': '''
            query GetDexTrades($first: Int, $token0: String!, $token1: String! $date: ISO8601DateTime!) {
                ethereum(network: matic) {
                    dexTrades(
                        options: { limit: $first, desc: "timeInterval.minute" }
                        baseCurrency: { is: $token1 }
                        quoteCurrency: { is: $token0 }
                        date: {since: $date }
                    ) {
                        timeInterval {
                            minute(format: "%FT%TZ", count: 60)
                        }
                        volume: quoteAmount
                        high: quotePrice(calculate: maximum)
                        low: quotePrice(calculate: minimum)
                        open: minimum(of: block, get: quote_price)
                        close: maximum(of: block, get: quote_price)
                    }
                }
            }
        ''',
        'variables': {
            'first': lookBack,
            'token0': token0,
            'token1': token1,
            'date': date
        },
        'operationName': 'GetDexTrades',
    }

    returnData = []
    response = requests.post('https://graphql.bitquery.io/',
                             headers=headerss, json=json_data).json()['data']['ethereum']['dexTrades']
    for data in response:
        date_string = data['timeInterval']['minute']
        date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
        timestamp = int(date_object.timestamp())
        returnData.append({
            'time': timestamp,
            'price': float(data['high']),
        })
    returnData = returnData[::-1]
    return returnData

pairAddressdump = {}
token0Dump = {}

@polygon_quickswap.get("/tokensInfo")
async def tokensInfo(token0: str = "", token1: str = ""):
    token0 = token0.lower()
    token1 = token1.lower()
    matic_price = float(requests.get("https://api.binance.com/api/v3/ticker/price?symbol=MATICUSDT").json()['price'])

    token0 = token0.lower()
    token1 = token1.lower()
    token0Contract = web3.eth.contract(
        abi=pairAbi, address=Web3.to_checksum_address(token0))
    token0TotalSupply = token0Contract.functions.totalSupply().call()
    token1Contract = web3.eth.contract(
        abi=pairAbi, address=Web3.to_checksum_address(token1))
    token1TotalSupply = token1Contract.functions.totalSupply().call()

    json_data = {
        'query': '''
              query swapsQuery($token0: String!, $token1: String!) {
                token0: tokens(orderDirection: desc, where: {id: $token0}) {              
                    id
                    symbol
                    name
                    decimals
                    totalSupply
                    totalValueLockedUSD
                    derivedMatic
                    volumeUSD
                }
                token1: tokens(orderDirection: desc, where: {id: $token1}) {
                    id
                    symbol
                    name
                    decimals
                    totalSupply
                    totalValueLockedUSD
                    derivedMatic
                    volumeUSD
                }
              }
            ''',
        'variables': {
            'token0': token0,
            'token1': token1
        },
        'operationName': 'swapsQuery',
    }

    response = requests.post('https://api.thegraph.com/subgraphs/name/sameepsi/quickswap-v3',
                             headers=headers, json=json_data).json()['data']

    response = {
        response['token0'][0]['id'].lower():
            {
                'symbol': response['token0'][0]['symbol'],
                'name': response['token0'][0]['name'],
                'mCap': int(token0TotalSupply / 10 ** float(response['token0'][0]['decimals']) * float(
                    response['token0'][0]['derivedMatic']) * matic_price),
                'volume': int(float(response['token0'][0]['volumeUSD'])),
                'tvl': int(float(response['token0'][0]['totalValueLockedUSD'])),
                'price': float(response['token0'][0]['derivedMatic']) * matic_price
            },
        response['token1'][0]['id'].lower():
            {
                'symbol': response['token1'][0]['symbol'],
                'name': response['token1'][0]['name'],
                'mCap': int(token1TotalSupply / 10 ** float(response['token1'][0]['decimals']) * float(
                    response['token1'][0]['derivedMatic']) * matic_price),
                'volume': int(float(response['token1'][0]['volumeUSD'])),
                'tvl': int(float(response['token1'][0]['totalValueLockedUSD'])),
                'price': float(response['token1'][0]['derivedMatic']) * matic_price
            },
        'pairTvl': int(
            float(response['token1'][0]['totalValueLockedUSD']) + float(response['token0'][0]['totalValueLockedUSD']))
    }
    return response


@polygon_quickswap.get("/topTokens")
async def topTokens(count: int = 50):
    json_data = {
        'query': "\n  query topTokens($first: Int) {\n  tokens(orderBy:txCount, orderDirection:desc, first:$first) { \n    id\n  }\n}",
        'variables': {
            'first': count,
            'operationName': 'topTokens'
        }
    }
    response = requests.post('https://api.thegraph.com/subgraphs/name/sameepsi/quickswap-v3',
                             headers=headers, json=json_data).json()['data']['tokens']
    response = [r['id'] for r in response]
    return response
