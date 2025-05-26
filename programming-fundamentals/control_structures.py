# Control Structures / Control Flow

instance_running = "running"

# If statements
if instance_running == "running":
    # Code to execute if condition is True
    print("The EC2 instance is running.")
elif instance_running == "stopped":
    # Code to execute if another_condition is True
    print("The EC2 instance is stopped.")
else:
    # Code to execute if none of the above conditions are True
    print("The EC2 instance is in an unknown state.")

public_access_blocked = True
# If-else statements
if public_access_blocked:
    print("Public access is blocked for the S3 bucket.")
else:
    print("Public access is allowed for the S3 bucket.")