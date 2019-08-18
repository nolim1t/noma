"""
config.py defines configuration of filesystem structure

Pathlib objects represent PosixPaths
"""
from pathlib import Path

# These constants are not to be changed during runtime
"""Filesystem"""
MEDIA_PATH = Path("/media")

NOMA_PATH = MEDIA_PATH / "noma"
COMPOSE_MODE_PATH = NOMA_PATH / "compose" / "neutrino"

LND_PATH = NOMA_PATH / "lnd"
BITCOIND_PATH = NOMA_PATH / "bitcoind"

HOME_PATH = Path.home()

"""LND Settings"""
LND_MODE = "neutrino"

"""LND Paths"""
TLS_CERT_PATH = LND_PATH / LND_MODE / "tls.cert"
SEED_FILENAME = LND_PATH / "seed.txt"

# Save password control file (Add this file to save passwords)
SAVE_PASSWORD_CONTROL_FILE = LND_PATH / "save_password"

# Create password for writing
TEMP_PASSWORD_FILE_PATH = LND_PATH / "password.txt"

SESAME_PATH = LND_PATH / "sesame.txt"

"""LND Endpoints"""
# Generate seed
URL_GENSEED = "https://127.0.0.1:8080/v1/genseed"

# Initialize wallet
URL_INITWALLET = "https://127.0.0.1:8080/v1/initwallet"


dirs = {'media': MEDIA_PATH,
        'noma': NOMA_PATH,
        'compose': COMPOSE_MODE_PATH,
        'lnd': LND_PATH,
        'tls_cert': TLS_CERT_PATH,
        'temp_pass': TEMP_PASSWORD_FILE_PATH,
        'save_pass': SAVE_PASSWORD_CONTROL_FILE,
        'seed': SEED_FILENAME,
        'sesame': SESAME_PATH,
        'bitcoind': BITCOIND_PATH,
        'home': HOME_PATH}

lnd = {'mode': LND_MODE,
       'genseed': URL_GENSEED,
       'initwallet': URL_INITWALLET}