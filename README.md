# Coinbase AlphaSquared Trader

Coinbase AlphaSquared Trader is a Python-based automated trading tool that integrates Coinbase Advanced Trading with AlphaSquared indicators. This project simplifies the process of creating and executing algorithmic trading strategies on Coinbase using AlphaSquared's risk assessment and strategy recommendations.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/coinbase-alphasquared-trader.git
   cd coinbase-alphasquared-trader
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Create a `config.json` file in the project root directory with the following structure:

```json
{
"coinbase_api_key": "YOUR_COINBASE_API_KEY",
"coinbase_api_secret": "YOUR_COINBASE_API_SECRET",
"alphasquared_api_key": "YOUR_ALPHASQUARED_API_KEY",
"product_id": "BTC-USD",
"strategy_name": "My Custom Strategy"
}
```

Replace the placeholder values with your actual API keys and desired trading configuration.

## Usage

To run the trader with the default configuration:

```python
from coinbase_alphasquared_trader import AlphaSquaredTrader, load_config
config = load_config('config.json')
trader = AlphaSquaredTrader(config)
trader.execute_strategy()
```

For more advanced usage and customization options, please refer to the documentation.

## Testing

To run the unit tests:
```bash
python -m unittest discover tests
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This software is for educational purposes only. Use at your own risk. The authors and contributors are not responsible for any financial losses incurred through the use of this software.