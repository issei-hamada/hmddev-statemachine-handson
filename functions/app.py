from logging import getLogger, INFO, Formatter

logger = getLogger()
logger.setLevel(INFO)
formatter = Formatter(
    '[%(levelname)s]\t%(asctime)s.%(msecs)dZ\t%(aws_request_id)s\t%(funcName)s\t%(message)s\n',
    '%Y-%m-%dT%H:%M:%S'
)


def lambda_handler(event, context):
    logger.info(f'{event=}')

    return {
        "Subject": 'Test',
        "Message": 'Hello, world!'
    }
