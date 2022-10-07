# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.

# def make_readable(seconds):
#     m = seconds // 60
#     s = seconds % 60
#     h = 0
#     if m >= 60:
#         h = seconds // 3600
#         m = m - h*60
#     if h < 10:
#         h = '0'+ str(h)
#     if s < 10:
#         s = '0'+str(s)
#     if m < 10:
#         m = '0'+str(m)
#
#     return f'{h}:{m}:{s}'
#
# print(make_readable(9))


def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

print(make_readable(56))