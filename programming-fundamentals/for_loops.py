# For Loops

instance_ids = [
    'i-1234567890abcdef0',
    'i-0987654321fedcba0',
    'i-11223344556677889'
]

for instance_id in instance_ids:
    print(f"Checking Status of EC2 Instance ID: {instance_id}")
    # Code to check the status of the instance
    print(f"Instance {instance_id} status check complete")
    
print('All instances checked successfully.\n')