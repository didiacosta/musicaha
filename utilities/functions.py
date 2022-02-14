from datetime import *
import sys,os
from log_error.models import Excepciones

class Functions:

	@staticmethod
	def toLog(e, modulo):
		ahora = datetime.now()
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		exepcion = Excepciones();
		message = str(e)
		exepcion.error = ('\n'+ str(ahora) + '--> ' + str(fname) +\
			' linea ' + str(exc_tb.tb_lineno) + ' --> ' + modulo + ': ' + message)
		exepcion.modulo = modulo
		exepcion.save()