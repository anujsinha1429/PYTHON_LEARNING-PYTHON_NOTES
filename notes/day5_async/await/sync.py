import time

def task():
    print("task started")
    time.sleep(3)
    print("task ended")

print("before task")
task ()
print("after task")



# output:

# before task
# task started
# (waits for 3 seconds)
# task ended
# after task

# sync program ko block kr deta h jab tk koi task complete na ho jaye