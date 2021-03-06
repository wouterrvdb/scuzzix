import datetime

# Default values

HOURS_PER_DAY = 8
HOUR_LIMIT = 2 * 30 * HOURS_PER_DAY

AMOUNT_OF_PMS = 1
AMOUNT_OF_WORKERS = 10

WORKER_COST = 5  # Cost for a worker each hour
DAY_COST = 100  # Cost for working an extra day

MAX_DURATION = HOURS_PER_DAY * 88   # Max duration of the project
SLACK = 7 * HOURS_PER_DAY           # Time we would like to have left before finishing the project

FLUCTUATION_COST = 1    # Cost for fluctuating workers
FLUCTUATION_LIMIT = AMOUNT_OF_WORKERS/10

START_DATE = datetime.datetime(2018, 9, 12, hour=9)   # Start first of July 2018
