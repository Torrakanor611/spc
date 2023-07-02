from spc.spc import spc

# hand made
data = [1001.2, 1003.4, 1002.4, 1000.8, 999.6, 1000.4]
T = 1000.0
sl = 45
n = 3

#
data1 = [                   # mean      range
    2501, 2461, 2512, 2468, # 2485.5    51
    2416, 2602, 2482, 2526, # 2506.5    186
    2487, 2494, 2428, 2443, # 2463      66
    2471, 2462, 2504, 2499, # 2484      42
    2510, 2543, 2464, 2531, # 2512      79
    2558, 2412, 2595, 2482, # 2511.75   183
    2518, 2540, 2555, 2461, # 2518.5    94
    2481, 2540, 2569, 2571, # 2540.25   90
    2504, 2599, 2634, 2590, # 2581.75   130
    2541, 2463, 2525, 2559, # 2522      96
    2556, 2457, 2554, 2588, # 2538.75   131
    2544, 2598, 2531, 2586, # 2564.75   67
    2591, 2644, 2666, 2678, # 2644.75   127
    2353, 2373, 2425, 2410, # 2390.25   65
    2460, 2509, 2433, 2511, # 2478.25   79
    2447, 2490, 2477, 2498, # 2478      51
    2523, 2579, 2488, 2481, # 2517.75   98
    2558, 2472, 2510, 2540, # 2520      88
    2579 ,2644, 2394, 2572, # 2547.25   250
    2446, 2438, 2453, 2475, # 2453      37
    2402, 2411, 2470, 2499, # 2445.5    97
    2551, 2454, 2549, 2584, # 2534.5    130
    2590, 2600, 2574, 2540  # 2576      60
]
T1 = 2500
sl1 = 500
n1 = 4
# cp = 1.75
# cpk = 1.65

def test_spc() -> None:
    data = [200, 201, 202, 203]
    T = 201
    sl = 2
    # n = 6 default
    test = spc(data, T, sl)
    assert test.data == data
    assert test.t == T
    assert test.sl == sl
    assert test.n == 6

def test_calc_capability() -> None:
    t = spc(data, T, sl, n)
    assert t.calc_capability() == 7.47

    t1 = spc(data1, T1, sl1, n1)
    assert t1.calc_capability() == 1.75

def test_calc_capability_index() -> None:
    t = spc(data, T, sl, n)
    assert t.calc_capability_index() == 7.04

    t1 = spc(data1, T1, sl1, n1)
    assert t1.calc_capability_index() == 1.65