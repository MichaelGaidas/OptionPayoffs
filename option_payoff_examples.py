from option_payoffs import *


def iron_condor_long_example():

    underlying_price = 100

    strike_price_long_put = 100
    premium_long_put = 2.10

    strike_price_short_put = 95
    premium_short_put = 0.70

    strike_price_long_call = 105
    premium_long_call = 2.35

    strike_price_short_call = 110
    premium_short_call = 0.95

    
    stock_price_range = np.arange(0.50*underlying_price, 1.50*underlying_price)
  
    iron_condor_net =  iron_condor(underlying_price, strike_price_long_put, premium_long_put,
                                  strike_price_short_put,  premium_short_put,
                                  strike_price_short_call, premium_short_call,
                                  strike_price_long_call,  premium_long_call,
                                  stock_price_range, False)

def iron_condor_short_example():
    underlying_price = 100

    strike_price_long_put = 95
    premium_long_put = 0.70

    strike_price_short_put = 100
    premium_short_put = 2.10

    strike_price_long_call = 110
    premium_long_call = 0.95

    strike_price_short_call = 105
    premium_short_call = 2.35

    
    stock_price_range = np.arange(0.50*underlying_price, 1.50*underlying_price)
  
    iron_condor_net =  iron_condor(underlying_price, strike_price_long_put, premium_long_put,
                                  strike_price_short_put,  premium_short_put,
                                  strike_price_short_call, premium_short_call,
                                  strike_price_long_call,  premium_long_call,
                                  stock_price_range, True)

def long_strangle_example():
    underlying_price = 50
    strike_price_call = 52
    premium_call = 3
    strike_price_put = 48
    premium_put = 2.85

    stock_price_range = np.arange(0.50*underlying_price, 1.50*underlying_price)

    long_strangle_net = strangle_or_straddle(underlying_price, strike_price_call, premium_call, strike_price_put, premium_put, stock_price_range, False)


def short_strangle_example():
    underlying_price = 50
    strike_price_call = 52
    premium_call = 3
    strike_price_put = 48
    premium_put = 2.85

    stock_price_range = np.arange(0.50*underlying_price, 1.50*underlying_price)

    short_strangle_net = strangle_or_straddle(underlying_price, strike_price_call, premium_call, strike_price_put, premium_put, stock_price_range, True)


def long_straddle_example():
    underlying_price = 15
    strike_price_call = 15
    premium_call = 2
    strike_price_put = 15
    premium_put = 1

    stock_price_range = np.arange(0.50*underlying_price, 1.50*underlying_price)

    long_straddle_example = strangle_or_straddle(underlying_price, strike_price_call, premium_call, strike_price_put, premium_put, stock_price_range, False)

def short_straddle_example():
    underlying_price = 15
    strike_price_call = 15
    premium_call = 2
    strike_price_put = 15
    premium_put = 1

    stock_price_range = np.arange(0.50*underlying_price, 1.50*underlying_price)

    short_straddle_example = strangle_or_straddle(underlying_price, strike_price_call, premium_call, strike_price_put, premium_put, stock_price_range, True)
    

def call_debit_spread_example():
    underlying_price = 49
    strike_price_long = 50
    premium_long = 2
    strike_price_short = 60
    premium_short = 1

    stock_price_range = np.arange(0.50*underlying_price, 1.50*underlying_price)

    cds = call_credit_or_debit_spread(underlying_price, strike_price_long, premium_long, strike_price_short, premium_short, stock_price_range, False)

def put_debit_spread_example():
    underlying_price = 30
    strike_price_long = 35
    premium_long = 4.75
    strike_price_short = 30
    premium_short = 1.75

    stock_price_range = np.arange(0.50*underlying_price, 1.50*underlying_price)

    pds = put_credit_or_debit_spread(underlying_price, strike_price_long, premium_long, strike_price_short, premium_short, stock_price_range, False)

def call_credit_spread_example():
    underlying_price = 240
    strike_price_short = 240
    premium_short = 5
    strike_price_long = 245
    premium_long = 2

    stock_price_range = np.arange(0.50*underlying_price, 1.50*underlying_price)

    cds_credit = call_credit_or_debit_spread(underlying_price, strike_price_long, premium_long, strike_price_short, premium_short, stock_price_range, True)

def put_credit_spread_example():
    underlying_price = 30
    strike_price_short = 30
    premium_short = 1
    strike_price_long = 28
    premium_long = 0.30

    stock_price_range = np.arange(0.50*underlying_price, 1.50*underlying_price)

    pds_credit = put_credit_or_debit_spread(underlying_price, strike_price_long, premium_long, strike_price_short, premium_short, stock_price_range, True)


def call_example(short=False, plot=True):
    underlying_price = 49
    strike_price = 50
    premium = 2

    stock_price_range = np.arange(0.50*underlying_price, 1.50*underlying_price)

    call = call_option(underlying_price, strike_price, premium, stock_price_range, short, plot)
    
def put_example(short=False, plot=True):
    underlying_price = 49
    strike_price = 50
    premium = 2

    stock_price_range = np.arange(0.50*underlying_price, 1.50*underlying_price)

    put = put_option(underlying_price, strike_price, premium, stock_price_range, short, plot)

