from oeqa.runtime.case import OERuntimeTestCase
from oeqa.core.decorator.depends import OETestDepends
from oeqa.core.decorator.oeid import OETestID

class BspRuntimeTest(OERuntime TestCase):

    @OETestID(001)
    def test_print_message():
        print "Hello World from Sangeeta"

