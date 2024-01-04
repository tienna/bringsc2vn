from pycardano import PaymentKeyPair, StakeKeyPair, Address, Network


payment_key_pair = PaymentKeyPair.generate()
payment_signing_key = payment_key_pair.signing_key
payment_verification_key = payment_key_pair.verification_key

stake_key_pair = StakeKeyPair.generate()
stake_signing_key = stake_key_pair.signing_key
stake_verification_key = stake_key_pair.verification_key

# Save
payment_signing_key.save("payment.skey")
payment_verification_key.save("payment.vkey")
stake_signing_key.save("stake.skey")
stake_verification_key.save("stake.vkey")
#payment_signing_key = payment_signing_key.load("payment.skey")
#payment_verification_key = payment_verification_key.load("payment.vkey")


network = Network.TESTNET
base_address = Address(payment_part=payment_verification_key.hash(),staking_part=stake_verification_key.hash(), network=network)
print(base_address);
