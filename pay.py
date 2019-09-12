from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString

# Create new seed with 'cat /dev/urandom |LC_ALL=C tr -dc 'A-Z9' | fold -w 81 | head -n 1'
seed = 'AQLJNGG9QNEFREDQPJR9TGUNZYRSJ9SQTUZWPIJYIIK9NKG9CPBMYFFDYPKEJKZTPOCUBSHZZA9XRFAOS'

# The Object
api = Iota('https://nodes.devnet.iota.org:443', seed)

# Address we are sending tokens to
address = 'FPPCJVXNYIJUFZGFPMZITTCKXQJDPTRBKLNQCZTZZYJDWFHTOMDRJXFXSYBUNWEABVATZOBELLMAYZPSBOIJLVJEG9'

print('Let there be light!\n'
      'Your current account-balance: ' + str(api.get_account_data()['balance']) + '\n'
      'How light du you want to buy (1sec = 1iota)? ', end='', flush=True)
tokens = input('iota: ')

tx = ProposedTransaction(
    address=Address(address),
    message=TryteString.from_unicode('Turn on the light'),
    tag=Tag('LIGHT'),
    value=int(tokens))

tx = api.prepare_transfer(transfers=[tx])

result = api.send_trytes(tx['trytes'], depth=3, min_weight_magnitude=9)
