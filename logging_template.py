
import logging

##########################################
# Example 1

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='tcp_server.log',
    filemode='w')


'''
Add the "logging.debug" statement as needed per example below
'''

if data[0] == 'say':
    logging.debug('Incoming message: {}'.format(data[0]))    # just add a statement like this.
    sc_conn.sendall(data[0].encode('utf-8'))



###################################
# Example 2

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S',
    #filename='tcp_server.log',
    #filemode='w',
    handlers=[
        logging.FileHandler("tcp_server.log"),
        logging.StreamHandler(sys.stdout)
    ])
# logging.getLogger().addHandler(logging.StreamHandler())


#############################
# Example 3
# using __name__ best convention

logger = logging.getLogger(__name__)

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S',
    #filename='tcp_server.log',
    #filemode='w',
    handlers=[
        logging.FileHandler("tcp_server.log"),
        logging.StreamHandler(sys.stdout)
    ])
# logging.getLogger().addHandler(logging.StreamHandler())


if data[0] == 'say':
    logger.debug('Incoming message: {}'.format(data[0]))
    sc_conn.sendall(data[0].encode('utf-8'))



##################
# Example 4

debug = True   # change to False to disable logging

logger = logging.getLogger(__name__)

def run_logging():
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S',
        #filename='tcp_server.log',
        #filemode='w',
        handlers=[
            logging.FileHandler("tcp_server.log"),
            logging.StreamHandler(sys.stdout)
        ])
    # logging.getLogger().addHandler(logging.StreamHandler())


if __name__ == '__main__':
    if debug:
        run_logging()

# ===================