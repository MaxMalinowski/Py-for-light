import time

from iota import Iota

# Create new seed with 'cat /dev/urandom |LC_ALL=C tr -dc 'A-Z9' | fold -w 81 | head -n 1'
seed = 'POLY9LOBHINTFCXVGTVVHWNBL9MKCQ9ONVHJVDVJKRNAMNQZZZYBXGR9HOKQLRLHQPMLCMBGYXHDRQYKR'

# The Object
api = Iota('https://nodes.devnet.iota.org:443', seed)

# Creating first address for the seed
addresses = api.get_new_addresses(index=0, count=1, security_level=2, checksum=True)
address = addresses['addresses'][0]

print('### Welcome to Pay for Light ###')
print('If you wish to have light, please send 5 iota.')
print('Address: ' + str(address) + '\n')
print('Waiting for payment ...', end='', flush=True)

waiting = True
balance_old = api.get_account_data()['balance']
while waiting:
    balance_new = api.get_account_data()['balance']
    if balance_new > balance_old:
        print('')
        for i in range(balance_new-balance_old):
            print(str(i+1), ' ############################################################################')
            time.sleep(1)
        waiting = False
    else:
        time.sleep(1)
        print('...', end='', flush=True)
