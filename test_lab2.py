import lab2temperature as lab2

def test_find_min_max():
    result=[]
    user_input = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
    result = [ 1 , 10 ]
    assert( result == lab2.calc_min_max_temperature(user_input) )

def test_calc_average():
    result = []
    user_input =  [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
    result = [ 5.5 ]
    assert( result == lab2.calc_average_temperature(user_input))

def test_calc_median_temperature():
    result = []
    user_input =  [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
    result = [ 5.5 ]
    assert (result == lab2.find_median_temperature(user_input))

