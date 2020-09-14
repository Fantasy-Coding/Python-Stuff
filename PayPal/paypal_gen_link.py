def paypal_gen_link(myemail_name, myemail_server, product_name, money_amount, currency_code):
    Link = ("https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=" + str(myemail_name) + "%40" + str(myemail_server) + "&item_name=" + str(product_name) + "&amount=" + str(money_amount) + "&currency_code=" + str(currency_code))
    return Link