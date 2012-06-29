d = {'K1': 'V1',   2 : 'V2',   'K3': 3,    4 : 4,  5 : 28,
    'K5' : {'abc1': { 456 : 45 },   "abc": { 123 : { '98.6' : 31 }}},
    'K6' : {'K7' : {'K8' : { 'K9':'K9'},  'K10':10, 11 : {11:'11', 12:12}}},
    '13' : {14 : 15, 141 : 31, 13 : 15, 142 : 31, 'abc': 12, 131 : '13'}
    }

import P1, P2

def main():
    print d
    result = P1.dict_to_list(d)
    print 'P1: ', result
    print 'P2: ', P2.find_index_optimized(result)


if __name__ == '__main__':
    main()
