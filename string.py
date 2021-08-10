# string
name = 'naisan'
print(name)     # naisan

full_name = 'naisan novel'
print(full_name[0])     # n
print(full_name[3])     # s
print(full_name[0:])   # naisan novel
print(full_name[0:3])   # nai

# copy one var string data to another
country = 'Bangladesh'
country_name = country[:]
print(country_name)        # Bangladesh

print(country_name.lower())     # bangladesh
print(country_name.upper())     # BANGLADESH

# f string
msg = f'i live in {country_name}'
print(msg)

print(country_name.find('d'))   # first matching index num
print(msg.replace('live in', 'love'))   # replace "live in" into "love"

is_include = 'live' in msg
print(is_include)   # return boolean value

print(msg.title())  # capitalize

