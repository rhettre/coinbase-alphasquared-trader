import unittest
from unittest.mock import Mock, patch
from decimal import Decimal
from coinbase_alphasquared_trader.trader import AlphaSquaredTrader

class TestAlphaSquaredTrader(unittest.TestCase):
    def setUp(self):
        self.coinbase_client = Mock()
        self.alphasquared_client = Mock()
        self.trader = AlphaSquaredTrader(self.coinbase_client, self.alphasquared_client)

    def test_execute_strategy_buy(self):
        self.alphasquared_client.get_current_risk.return_value = 50
        self.alphasquared_client.get_strategy_value_for_risk.return_value = ('buy', 100)
        self.coinbase_client.fiat_limit_buy.return_value = {'id': 'test_order_id'}

        self.trader.execute_strategy('BTC-USD', 'Test Strategy')

        self.coinbase_client.fiat_limit_buy.assert_called_once_with('BTC-USD', '100', price_multiplier='0.995')

    def test_execute_strategy_sell(self):
        self.alphasquared_client.get_current_risk.return_value = 80
        self.alphasquared_client.get_strategy_value_for_risk.return_value = ('sell', 5)
        self.coinbase_client.get_crypto_balance.return_value = '1.0'
        self.coinbase_client.get_product.return_value = {
            'base_increment': '0.00000001',
            'quote_increment': '0.01',
            'price': '50000'
        }
        self.coinbase_client.limit_order_gtc_sell.return_value = {'id': 'test_order_id'}

        self.trader.execute_strategy('BTC-USD', 'Test Strategy')

        self.coinbase_client.limit_order_gtc_sell.assert_called_once()

    def test_execute_strategy_no_action(self):
        self.alphasquared_client.get_current_risk.return_value = 50
        self.alphasquared_client.get_strategy_value_for_risk.return_value = ('hold', 0)

        self.trader.execute_strategy('BTC-USD', 'Test Strategy')

        self.coinbase_client.fiat_limit_buy.assert_not_called()
        self.coinbase_client.limit_order_gtc_sell.assert_not_called()

if __name__ == '__main__':
    unittest.main()