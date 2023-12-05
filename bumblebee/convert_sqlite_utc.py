# Sqlite data in linux epoch time. Convert to UTC
# In SQLITE: can run
# SELECT datetime(1682424941, 'unixepoch', 'utc');

import datetime, sys

timestamp = int(sys.argv[1])
utc_time = datetime.datetime.utcfromtimestamp(timestamp)

# Format the UTC time
formatted_time = utc_time.strftime("%d/%m/%y %H:%M:%S")
print("Original UTC Time:", formatted_time)

# Subtract 1 hour from the UTC time
one_hour_less = utc_time - datetime.timedelta(hours=1)
formatted_one_hour_less = one_hour_less.strftime("%d/%m/%y %H:%M:%S")
print("One Hour Less UTC Time:", formatted_one_hour_less)

