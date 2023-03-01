import gauss_functions

def test_get_correct_x_coeficient():
   assert gauss_functions.obterCoefX("2.0x + 4.0y = 8.0") == 2.0

def test_get_correct_y_coeficient():
   assert gauss_functions.obterCoefY("2.0x + 4.0y = 8.0") == 4.0