import logging
from logging.handlers import RotatingFileHandler

def returnRthandler():
	Rthandler = RotatingFileHandler(
		'filename.log',
		maxBytes = 1*1024*1024,
		backupCount = 3)
	Rthandler.setLevel(logging.INFO)
	formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
	Rthandler.setFormatter(formatter)
	return Rthandler

Rthandler = returnRthandler()
logging.getLogger('').addHandler(Rthandler)
logging.warning("hello")