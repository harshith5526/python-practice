def is_leap(year):
  leap=False
  #applying condition for checking given year is leap year or not
  if(year%400==0) or (year%4==0 and year%100!=0):
    # if the year is leap returns true
    returnTrue
  else:
    return False
  return leap
year=int(input())
print(is_leap(year))
  
