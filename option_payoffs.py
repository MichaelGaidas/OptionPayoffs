import numpy as np
import matplotlib.pyplot as plt
from option_payoff_examples import *
plt.style.use('ggplot')

def create_plot(net_payoff_list, stock_price_range, title, max_gain=0, max_loss=0, breakeven=0):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.spines['bottom'].set_position('zero')

    for i in range(len(net_payoff_list)):
        if( (len(net_payoff_list) > 1 and i == len(net_payoff_list) - 1) or len(net_payoff_list) == 1):
            ax.plot(stock_price_range, net_payoff_list[i][0], label=net_payoff_list[i][1])
        else:
            ax.plot(stock_price_range, net_payoff_list[i][0], '--', label=net_payoff_list[i][1])


    format_max_gain = "Max Gain: $" + str('{:6.2f}').format(max_gain) if type(max_gain) != str else "Max Gain: $inf"
    format_max_loss = "Max Loss: $" + str('{:6.2f}').format(max_loss) if type(max_loss) != str else "Max Loss: $inf"
                
    ax.text(0.5, -0.10, format_max_gain, horizontalalignment='center', verticalalignment='center', color='green', transform=ax.transAxes)
    ax.text(0.5, -0.05, format_max_loss, horizontalalignment='center', verticalalignment='center', color='red', transform=ax.transAxes)  
    
    for i in range(len(breakeven)):
        ax.text(0.75, (-0.10 / float(i + 1)), "Breakeven Price: $" + str('{:6.2f}').format(breakeven[i]), horizontalalignment='center', verticalalignment='center', color='black', transform=ax.transAxes)
 
    plt.xlabel('Stock Price')
    plt.ylabel('Profit / Loss')
    plt.title(title)
    plt.legend()
    plt.show()


def spread_gains(strike_price_long, premium_long, strike_price_short, premium_short, credit=True):
    max_gain = abs((premium_short - premium_long) * 100) if credit else (abs(strike_price_long - strike_price_short) - abs(premium_short - premium_long)) * 100
    max_loss = (abs(strike_price_long - strike_price_short) - abs(premium_short - premium_long)) * 100 if credit else abs((premium_short - premium_long) * 100)
    return max_gain, max_loss

def call_or_put_gain_loss_breakeven(strike_price, premium, call=True, short=False):
    breakeven = strike_price + premium if call else strike_price - premium
    max_gain = "inf" if not short else premium
    max_loss = premium if not short else "inf"
    
    if(call):
        line_name = 'Short Call' if short else 'Long Call'
    else:
        line_name = 'Short Put' if short else 'Long Put'    

    return line_name, max_gain, max_loss, breakeven

# set plot = True if you want to see the individual payoff for spreads
def call_option(underlying_price, strike_price, premium, stock_price_range, short=False, plot=False):
    
    profit_loss = [value - strike_price - premium if value > strike_price else 0 - premium for value in stock_price_range]
    profit_loss = np.negative(profit_loss) if short else profit_loss

    if(plot):
        line_name, max_gain, max_loss, breakeven = call_or_put_gain_loss_breakeven(strike_price, premium, True, short)
        create_plot([(profit_loss, line_name)], stock_price_range, line_name, max_gain, max_loss, [breakeven])
        
    return profit_loss

# set plot = True if you want to see the individual payoff for spreads
def put_option(underlying_price, strike_price, premium, stock_price_range, short=False, plot=False):
    
    profit_loss = [strike_price - value - premium if strike_price > value else 0 - premium for value in stock_price_range]
    profit_loss = np.negative(profit_loss) if short else profit_loss

    if(plot):
        line_name, max_gain, max_loss, breakeven = call_or_put_gain_loss_breakeven(strike_price, premium, False, short)
        create_plot([(profit_loss, line_name)], stock_price_range, line_name, max_gain, max_loss, [breakeven])
   
    return profit_loss 



# AKA - Bear Call Spread or Bull Call Spread
def call_credit_or_debit_spread(underlying_price, strike_price_long, premium_long, strike_price_short, premium_short, stock_price_range, credit=True):
    net_payoff_list = []
    str_credit_or_debit = 'Call Credit Spread' if credit else 'Call Debit Spread'

    short_call_payoff = call_option(underlying_price, strike_price_short, premium_short, stock_price_range, True, False) 
    net_payoff_list.append((short_call_payoff, 'Short Call'))

    long_call_payoff = call_option(underlying_price, strike_price_long, premium_long, stock_price_range, False, False)
    net_payoff_list.append((long_call_payoff, 'Long Call'))

    call_credit_payoff = np.add(long_call_payoff, short_call_payoff) 
    net_payoff_list.append((call_credit_payoff, str_credit_or_debit))
        
    max_gain, max_loss = spread_gains(strike_price_long, premium_long, strike_price_short, premium_short, credit)
    breakeven = strike_price_short + premium_short - premium_long if credit else strike_price_long + premium_long - premium_short
    
    create_plot(net_payoff_list, stock_price_range, str_credit_or_debit, max_gain, max_loss, [breakeven])

    return call_credit_payoff



# AKA Bull Put Spread or Bear Put Spread
def put_credit_or_debit_spread(underlying_price, strike_price_long, premium_long, strike_price_short, premium_short, stock_price_range, credit=True):
    net_payoff_list = []
    str_credit_or_debit = 'Put Credit Spread' if credit else 'Put Debit Spread'

    short_put_payoff = put_option(underlying_price, strike_price_short, premium_short, stock_price_range, True, False)
    net_payoff_list.append((short_put_payoff, 'Short Put'))

    long_put_payoff = put_option(underlying_price, strike_price_long, premium_long, stock_price_range, False, False)
    net_payoff_list.append((long_put_payoff, 'Long Put'))

    put_credit_payoff = np.add(long_put_payoff, short_put_payoff)
    net_payoff_list.append((put_credit_payoff, str_credit_or_debit))


    max_gain, max_loss = spread_gains(strike_price_long, premium_long, strike_price_short, premium_short, credit)
    breakeven = strike_price_short + premium_long - premium_short if credit else strike_price_long + premium_short - premium_long

    
    create_plot(net_payoff_list, stock_price_range, str_credit_or_debit, max_gain, max_loss, [breakeven])


    return put_credit_payoff

def strangle_or_straddle(underlying_price, strike_price_call, premium_call, strike_price_put, premium_put, stock_price_range, short=False):
    net_payoff_list = []
    str_short_or_long_title = 'Short Strangle or Straddle' if short else 'Long Strangle or Straddle'
    str_short_or_long_call = 'Short Call' if short else 'Long Call'
    str_short_or_long_put = 'Short Put' if short else 'Long Put'
    

    long_call_payoff = call_option(underlying_price, strike_price_call, premium_call, stock_price_range, short, False) # put in a bool for long or short straddle
    net_payoff_list.append((long_call_payoff, str_short_or_long_call))

    long_put_payoff = put_option(underlying_price, strike_price_put, premium_put, stock_price_range, short, False)
    net_payoff_list.append((long_put_payoff, str_short_or_long_put))

    strangle_payoff = np.add(long_call_payoff, long_put_payoff)
    net_payoff_list.append((strangle_payoff, str_short_or_long_title))

    max_gain = "inf" if not short else (premium_call + premium_put) * 100
    max_loss = (premium_call + premium_put) * 100 if not short else 'inf'
    breakeven_call = strike_price_call + premium_call + premium_put
    breakeven_put = strike_price_put - premium_put - premium_call
    
    create_plot(net_payoff_list, stock_price_range, str_short_or_long_title, max_gain, max_loss, [breakeven_call, breakeven_put])    

    return net_payoff_list

    
# Long Iron Condor - Bear Put Spread and Bull Call Spread -v-
# Short Iron Condor - Bull Put Spread and Bear Call Spread -^- 
def iron_condor(underlying_price, strike_price_long_put,   premium_long_put,
                                  strike_price_short_put,  premium_short_put,
                                  strike_price_short_call, premium_short_call,
                                  strike_price_long_call,  premium_long_call,
                                  stock_price_range, short=False):

    net_payoff_list = []
    str_short_or_long_title = "Short Iron Condor" if short else "Long Iron Condor"

    long_put_payoff = put_option(underlying_price, strike_price_long_put, premium_long_put, stock_price_range, False, False)
    short_put_payoff = put_option(underlying_price, strike_price_short_put, premium_short_put, stock_price_range, True, False)

    long_call_payoff = call_option(underlying_price, strike_price_long_call, premium_long_call, stock_price_range, False, False)
    short_call_payoff = call_option(underlying_price, strike_price_short_call, premium_short_call, stock_price_range, True, False)

    iron_condor_payoff_put = np.add(long_put_payoff, short_put_payoff)
    iron_condor_payoff_call = np.add(long_call_payoff, short_call_payoff)

    iron_condor_payoff = np.add(iron_condor_payoff_put, iron_condor_payoff_call)
    net_payoff_list.append((iron_condor_payoff, 'Iron Condor'))

    
    net_debit = (premium_long_put + premium_long_call) - (premium_short_put + premium_short_call)
    net_credit = (premium_short_put + premium_short_call) - (premium_long_put + premium_long_call)
    
    spread_width_puts = abs(strike_price_long_put - strike_price_short_put)
    spread_width_calls = abs(strike_price_long_call - strike_price_short_call)

    max_spread = spread_width_puts if spread_width_puts >= spread_width_calls else spread_width_calls
  
    max_gain = (max_spread - net_debit) * 100 if not short else net_credit * 100
    max_loss = net_debit * 100 if not short else (max_spread - net_credit) * 100

    breakeven_upper = strike_price_long_call + net_debit if not short else strike_price_short_call + net_credit
    breakeven_lower = strike_price_long_put - net_debit if not short else strike_price_short_put - net_credit

    create_plot(net_payoff_list, stock_price_range, str_short_or_long_title, max_gain, max_loss, [breakeven_upper, breakeven_lower]) 
    
    return net_payoff_list

if __name__ == "__main__":

    call_example()
    put_example()

    put_debit_spread_example()6
    put_credit_spread_example()

    call_debit_spread_example()
    call_credit_spread_example()

    long_strangle_example()
    short_strangle_example()

    long_straddle_example()
    short_straddle_example()

  
    iron_condor_long_example()
    iron_condor_short_example()












