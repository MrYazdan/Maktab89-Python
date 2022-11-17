# MUTABLE
a_list = [1, 2, 3, 4, 5]

# IMMUTABLE
a_tuple = (1, 2, 3, 4, 5)

# Test:
a_list[4] = 10

# a_tuple[4] = 10

# from pprint import pprint
# pprint(data)

datas = {
    'ages': [10, 20, 33, 18, 7, 12, 36],
    99: range(0, 100),
    (1, 2): ('one', 'two'),
    'data': {
        'ages': [10, 20, 33, 18, 7, 12, 36],
        99: range(0, 100),
        (1, 2): ('one', 'two'),
        'data': {
            'ages': [10, 20, 33, 18, 7, 12, 36],
            99: range(0, 100),
            (1, 2): ('one', 'two'),
            'data': {
                'ages': [10, 20, 33, 18, 7, 12, 36],
                99: range(0, 100),
                (1, 2): ('one', 'two'),
                # [1, 2, 3]: 'test'
            }
        }
    }
}

# 1
# print(datas['age'])
# print(datas['ages'])
# print(datas['ages'])
# print(datas['data']['data']['data'])

# 2
# print(datas.get('ages'))
# print(datas.get('ages', []))

# 3
# TODO : Search it !!!
# print(getattr(datas, 'ages'))
# setattr(datas, 'ages')

data = {
    'alpha_lower': list('abcdefghijklmnopqrstuvwxyz'),
    'alpha_upper': list('abcdefghijklmnopqrstuvwxyz'.upper()),
    'digits': list('0123456789')
}

# key -> value
# for x in data:
# for x in data.values():
# for k, v in data.items():
#     print(len(v))

# first_name, last_name, age, phone

# first_name, last_name, age, phone = tuple(input("> ").split(','))

# profile = {
#     "first_name": first_name,
#     "last_name": last_name,
#     "age": age,
#     "phone": phone,
# }

# for k, v in profile.items():
#     print(f"{k}: {v}", end='\n' + '-' * 20 + '\n')

# def power(n, pi):
#     return n ** pi

# print(power(2, 6))

# power = lambda n, pi: n ** pi

ages = [10, 12, 56, 18, 102, 34, 13, 16, 9]

# 1
# def adult(age):
#     if age < 18:
#         return False
#     else:
#         return True

# return False if age < 18 else True

# valid_ages = []
# for age in ages:
#     if adult(age):
#         valid_ages.append(age)
#
# print(valid_ages)

# 2
# print(list(map(adult, ages)))

# 3

# print(list(map(lambda x: False if x < 18 else True, ages)))

# 4
# print(filter(lambda x: 1 if x < 18 else 0, ages))
# print(data['digits'])
# print(list(map(int, filter(int, data['digits']))))
#

# valid_ages = []
# for age in ages:
#     if age >= 18:
#         valid_ages.append(age)

# adult_ages = [age for age in ages if age >= 18]
# adult_ages = [age for age in range(1, 20)]
# adult_ages = [num for num in range(1, 20) if num % 2 == 0]
adult_ages = [num if num % 2 == 0 else '' for num in range(1, 20)]
data2 = {data['alpha_upper'][num]: num for num in range(1, 20)}

# print(valid_ages)
# print(adult_ages)
print(data2)
