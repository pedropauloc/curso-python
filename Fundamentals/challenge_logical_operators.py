# challenge logical operators

# The jobs
work_tuesday = True
work_thursday = False

"""
- Confirmed Both: TV 50' + Ice cream
- Confirmed only one: TV 32' + Ice cream
- None confirmed: Stay home
"""

tv_50 = work_tuesday and work_thursday
ice_cream = work_tuesday or work_thursday
tv_32 = work_tuesday != work_thursday
healthier = not ice_cream

print('Tv50 = {} Tv32 = {} IceCream = {} Healthier = {}'.format(tv_50, tv_32, ice_cream, healthier))