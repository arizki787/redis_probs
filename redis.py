import time
import random

def call_redis():
    time.sleep(0.5)
    rates = call_db()
    return rates

def new_layer_update_local_rates():
    #this function call redis and save to local memory
    #check if every minute has changes. if minutes changes call to redis. with margin error (always up)
    when_to_change = random.randint(1,10) 
    # when_to_change = 5 

    if when_to_change == 5: #asumsikan setiap 5 menit
        price = call_redis()
        new_price = {key: value * 1.01 for key, value in price.items()}
    else:
        old_price = {    
            "usd-idr": 18000,
            "sgd-idr": 10000,
        }

        new_price = {key: value * 1.01 for key, value in old_price.items()}

    return new_price


def call_db():
    #get the exchange rate
    pair = {    
        "usd-idr": 18000,
        "sgd-idr": 10000,
    }

    rand_num = random.randint(1,3)

    new_dict = {key: value * rand_num for key, value in pair.items()}
    
    return new_dict


def this_app():
    local_rates = new_layer_update_local_rates()

    print(local_rates)


this_app()
    