'''<HANDLER DESCRIPTION>'''

import logging
import json
import os
import random
import time

from iopipe.iopipe import IOpipe
from iopipe.contrib.profiler import ProfilerPlugin
from iopipe.contrib.trace import TracePlugin

# logging
log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))  # type:ignore
_logger = logging.getLogger(__name__)

# IOpipe
iopipe_profiler_enabled = os.environ.get('IOPIPE_PROFILER_ENABLED', '').lower() == 'true'
iopipe_profiler_plugin = ProfilerPlugin(enabled=iopipe_profiler_enabled)
iopipe_tracing_plugin = TracePlugin(auto_measure=True)

iopipe_token = os.environ.get('IOPIPE_TOKEN') or None
iopipe = IOpipe(iopipe_token,
                plugins=[iopipe_profiler_plugin, iopipe_tracing_plugin])


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

