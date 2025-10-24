from hedera import Client, AccountId, PrivateKey
import os

def get_client():
    """Connect to Hedera Testnet"""
    account_id = AccountId.fromString(os.getenv("HEDERA_ACCOUNT_ID"))
    private_key = PrivateKey.fromString(os.getenv("HEDERA_PRIVATE_KEY"))
    client = Client.for_testnet()
    client.setOperator(account_id, private_key)
    return client