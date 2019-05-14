from calendar import isleap
leapyears = {year for year in range(2016, 2066) if isleap(year)}
print('leapyear: ',leapyears)
