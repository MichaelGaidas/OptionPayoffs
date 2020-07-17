# OptionPayoffs
Visualizes the profit and loss graph of various option strategies - Python

## Installation
Download option_payoffs.py and add to your library. 
Will be added to pip once completed.

## Usage
```bash
import option_payoffs as op
import numpy as np

underlying_price = 50
strike_price_long_call = 50
premium_long_call = 2
stock_price_range = np.arange(0.50*underlying_price, 1.50*underlying_price)

long_call_option_payoff = op.call_option(underlying_price, strike_price_long_call,
                                         premium_long_call, stock_price_range, False, True) # False = Long, True = Plot

```

## Example Graph - Long Strangle

![alt text](https://github.com/MichaelGaidas/OptionPayoffs/blob/master/strangle_img.JPG)

## Contributing
Please feel free to pull and make any changes you want. This project is in progress, there may be quite a bit of bugs.
