# ------------------------------------------ Задание 1-------------------------------------------------------


def country_description(name, **kwargs):
    print(f'{name}')
    for i in kwargs:
        print(f'{i} - {kwargs[i]}')

country_description(name='USA', population='330 million', is_democratic=True)
country_description(name='Kyrgyzstan', area='200 km2', have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])


