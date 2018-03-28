'''<HANDLER DESCRIPTION>'''

import logging
import json
import os
import random
import time

log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))
_logger = logging.getLogger(__name__)

def handler(event, context):
    '''Function entry'''

    # random slow down.
    if random.randint(1, 10) > 8:
        _logger.info('Hit bottleneck....')
        time.sleep((100 - random.randint(5, 20)) / 100)


    if random.randint(1, 10) > 9:
        _logger.info('JACKPOT!!!')
        discount_multiplier = (100 - random.randint(5, 20)) / 100
    else:
        discount_multiplier = 1


    resp_body = {'DiscountMultiplier': discount_multiplier}

    resp = {
        'statusCode': 201,
        'body': json.dumps(resp_body)
    }
    return json.dumps(resp)

