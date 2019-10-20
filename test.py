import unittest
from operation_data import get_data
from ddt import ddt, data, unpack

@ddt
class FooTestCase(unittest.TestCase):
	cases_id = []
	cases_name = []
	ids = get_data.getData().get_case_count()
	for i in range(1, ids):
		if get_data.getData().get_is_run(i):
			cases_id.append(i)
			cases_name.append(get_data.getData().get_case_name(i))
	datas = list(zip(cases_id, cases_name))
	print(datas)

	@unpack
	@data(*datas)
	def test_dic(self, a,b):
		# print(a,b)
		self.assertTrue(2< 3 )


if __name__ == '__main__':
	unittest.main(verbosity=2)