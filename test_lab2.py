import lab2temperature

def test_find_min_max():
    result=[]
    user_input = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
    result = [min(user_input), max(user_input)]
    assert( result == lab2temperature.calc_min_max_temperature(user_input) )

    