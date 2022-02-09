# thegraph-graplml-wss-gql

Proof of concept demonstrating the trouble I'm having with **TheGraph graphml subscription websocket streaming via Python gql**

This example creates a GraphML subscription for swaps on Uniswap.

## Usage

```{bash}
python3 ./test_streaming.py
```

Expected result:

The WSS API returns the expected objects.

```{json}
  [{'id': '0x23d332b12fb3f751ea3dd568f12a6a84b10b3655d49886295975a8eca4794290',
    'swaps': [{'amountUSD': '195.3825540191495212816161158199149',
              'pair': {'token0': {'symbol': 'XXX'},
                        'token1': {'symbol': 'WETH'}}}],
    'timestamp': '1644432149'},
  {'id': '0x1f70f66aa7d096442e2f275d3e46060bc4917faef11b23797e60f7c003ba4d68',
    'swaps': [{'amountUSD': '15954.53116759447837387020011964246',
              'pair': {'token0': {'symbol': 'WETH'},
                        'token1': {'symbol': 'XXX'}}}],
    'timestamp': '1644432149'}]
```

But after about 10 seconds, the websocket is closed unexpectedly:

```{txt}
File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/asyncio/streams.py", line 721, in readexactly
    raise exceptions.IncompleteReadError(incomplete, n)
asyncio.exceptions.IncompleteReadError: 0 bytes read on a total of 2 expected bytes
```

## Install dependencies

```{bash}
make requirements
```

<!--
git clone \
  -c core.sshCommand="/usr/bin/ssh -o IdentitiesOnly=yes -i ~/.ssh/0xidm" \
  git@github.com:0xidm/0xidm.git

git config --local user.email "0xidm"
git config --local user.name "0xidm"
-->
