"""
Author: BlueBigThink
"""
import os
if os.path.exists(".env"):
    # if we see the .env file, load it
    from dotenv import load_dotenv
    load_dotenv()

OWNER_PRIVATE_KEY = os.getenv('OWNER_PRIVATE_KEY')
ETH_CONTRACT_ADDRESS = os.getenv('ETH_CONTRACT_ADDRESS')
BSC_CONTRACT_ADDRESS = os.getenv('BSC_CONTRACT_ADDRESS')
OWNER_ADDRESS = os.getenv('OWNER_ADDRESS')
INFURA_ID = os.getenv('INFURA_ID')
BOT_TOKEN = os.getenv('BOT_TOKEN')
ETH_MAINNET_ID = os.getenv('ETH_MAINNET_ID')
ETH_TESTNET_ID = os.getenv('ETH_TESTNET_ID')
BSC_MAINNET_ID = os.getenv('BSC_MAINNET_ID')
BSC_TESTNET_ID = os.getenv('BSC_TESTNET_ID')
MAIN_ETH_SCAN_URL = os.getenv('MAIN_ETH_SCAN_URL')
TEST_ETH_SCAN_URL = os.getenv('TEST_ETH_SCAN_URL')
MAIN_BSC_SCAN_URL = os.getenv('MAIN_BSC_SCAN_URL')
TEST_BSC_SCAN_URL = os.getenv('TEST_BSC_SCAN_URL')
TOKEN_CONTRACT_ADDRESS = os.getenv('TOKEN_CONTRACT_ADDRESS')
CONTRACT_ADDRESS = ETH_CONTRACT_ADDRESS

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PWD = os.getenv('DB_PWD')
DB_PORT = os.getenv('DB_PORT')
DB_DATABASE = os.getenv('DB_DATABASE')


