# idm

from pprint import pprint

from gql import gql, Client
from gql.transport.websockets import WebsocketsTransport

# https://thegraph.com/docs/en/developer/graphql-api/

query_txs = """subscription {
  transactions(orderBy: timestamp, orderDirection: desc) {
    id
    timestamp
    swaps(where: {amountUSD_gt:1}) {
      pair {
        token0 { symbol }
        token1 { symbol }
      }
      amountUSD
    }
  }
}
"""

transport = WebsocketsTransport(
    url='wss://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2',
    # keep_alive_timeout=10,
    # ping_interval=None,
    # pong_timeout=10,
    ping_interval=None,
    keep_alive_timeout=None,
)

client = Client(
    transport=transport,
    fetch_schema_from_transport=False,
)

query = gql(query_txs)

for result in client.subscribe(query):
    pprint(result)
