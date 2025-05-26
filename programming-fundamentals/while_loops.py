# # While loops in Python

# count = 0

# while count < 5:
#     print(f"Count is: {count}")
#     count += 1

import random
import time

def simulate_instance_state():
    states = ["pending", "pending", "pending", "running"]
    return random.choice(states)

instance_state = "pending"
attempts = 0

while instance_state != "running" and attempts < 5:
    print(f"Attempt {attempts + 1}: Instance state is '{instance_state}'. Waiting for it to become 'running'...")
    instance_state = simulate_instance_state()
    attempts += 1
    time.sleep(1)  # Simulate waiting time for the instance to change state

if instance_state == "running":
    print("Instance is now running.")
else:
    print("Instance did not reach 'running' state after 5 attempts. Instance did not start in time.")