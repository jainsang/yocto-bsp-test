from oeqa.runtime.case import OERuntimeTestCase
from oeqa.core.decorator.depends import OETestDepends
from oeqa.core.decorator.oeid import OETestID

class BspRuntimeTest(OERuntimeTestCase):

	@OETestID(124)
	def test_print_message(self):
		command = 'echo "Hello World from Sangeeta"'
		status, output = self.target.run(command)
		msg = ('testcase not working as expected. '
			'Status and output:%s and %s.' % (status, output))
		self.assertEqual(status, 0, msg = msg)
