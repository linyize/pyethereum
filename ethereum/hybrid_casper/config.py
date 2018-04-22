import copy
from ethereum import utils, config
from ethereum.tools.tester import a0

casper_config = dict(
    # The Casper-specific config declaration
    METROPOLIS_FORK_BLKNUM=0,
    ANTI_DOS_FORK_BLKNUM=0,
    CLEARING_FORK_BLKNUM=0,
    CONSENSUS_STRATEGY='hybrid_casper',
    EPOCH_LENGTH=50,
    NON_REVERT_MIN_DEPOSIT=10**18,
    SENDER=b'\xff' * 32,
    OWNER=a0,
    MIN_DEPOSIT_SIZE=1500 * 10**18,

    # IMO fork
    IMO_FORK_BLKNUM=1000000, # 100个块以后开始要求特殊的共识规则 
    IMO_FORK_MIN_MINER_BALANCE=1000, # coinbase必须有大于1000eth
    IMO_FORK_BLK_NOTREPEAT=10, # 10个块内不得出现重复的coinbase
    HOMESTEAD_FORK_BLKNUM = 2**99,
    SPURIOUS_DRAGON_FORK_BLKNUM = 2**99,
    DAO_FORK_BLKNUM = 2**99,
)

config.casper_config = {**config.default_config, **casper_config}
