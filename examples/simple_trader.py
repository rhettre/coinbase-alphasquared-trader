from coinbase_advanced_trader import EnhancedRESTClient
from alphasquared import AlphaSquared
from coinbase_alphasquared_trader import AlphaSquaredTrader, load_config

def main():
    config = load_config('config.json')
    
    coinbase_client = EnhancedRESTClient(
        api_key=config['coinbase_api_key'],
        api_secret=config['coinbase_api_secret']
    )
    
    alphasquared_client = AlphaSquared(
        api_key=config['alphasquared_api_key'],
        cache_ttl=config.get('cache_ttl', 60)
    )
    
    trader = AlphaSquaredTrader(coinbase_client, alphasquared_client)
    
    product_id = config['product_id']
    strategy_name = config['strategy_name']
    
    trader.execute_strategy(product_id, strategy_name)

if __name__ == "__main__":
    main()