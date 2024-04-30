import lab2

def test_calc_min_max_temperature():
    result=[]
    user_input = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ,8 , 9 , 10 ]
    result = [int(min(user_input)), int(max(user_input))]
    assert(result==lab2.calc_min_max_temperature(user_input))


