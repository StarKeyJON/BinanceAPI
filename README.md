Binance API - Websockets and Real-Time Lightweight Charts

Websockets and Real-Time Lightweight Charts
	wscat - connect to websocket from command line
		General WSS info: https://github.com/binance-us/binance-official-api-docs/blob/master/web-socket-streams.md#general-wss-information
                 wss://stream.binance.us:9443            
            capture output to a file
		connect to websocket from the Web / Javascript
	Lightweight Charts - create real-time candlestick chart similar to tradingview
		UI to check indicators, configure values/alerts/notifications

TA with Python and TALib
	connect to websockets from Python, write candlestick data to csv
		download historical data using REST API
		configure indicators

Backtesting with Backtrader and TALib Indicators
	test some indicators against a historical bakcing
	plot some buy and sell indicators

Building an API for indicators
	API endpoint to save / persist indicators
		using settings from Python websocket to detect actionable orders
			API endpoint for executing a buy/sell order
			API endpoint for sending notifications

