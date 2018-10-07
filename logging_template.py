
import logging

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
