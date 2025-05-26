# List of EC2 instances
instance_ids = [
    'i-1234567890abcdef0',
    'i-0987654321fedcba0',
    'i-11223344556677889'
]

# List of IP addresses for a securty group
ip_addresses = [
    '10.0.0.1',
    '10.0.0.2',
    '10.0.0.3',
    '10.0.0.4'
]

# List of availability zones in a region
availability_zones = [
    'eu-central-1a',
    'eu-central-1b',
    'eu-central-1c'
]

# Print the lists
print(f"EC2 Instance IDs: {instance_ids}")
print(f"Security Group IP Addresses: {ip_addresses}")
print(f"Availability Zones: {availability_zones}")

# Add new EC2 instance ID to the list
new_instance_id = 'i-22334455667788990'
instance_ids.append(new_instance_id)
print("After adding a new instance ID:")
print(f"EC2 Instance IDs: {instance_ids}")

# Remove an EC2 instance ID from the list
instance_ids.remove('i-0987654321fedcba0')
print("After removing an instance ID:")
print(f"EC2 Instance IDs: {instance_ids}")

# Check if an IP address exists in the list
ip_to_check = '10.0.0.4'
if ip_to_check in ip_addresses:
    print(f"IP address {ip_to_check} exists in the security group and allowed.")
else:
    print(f"IP address {ip_to_check} does not exist in the security group and is not allowed.")
print(f"Security Group IP Addresses: {ip_addresses}")

# Slicing a list
# Fetch the first two availability zones
first_two_azs = availability_zones[:2]
print(f"First two availability zones: {first_two_azs}")

# Sorting a list
# Sort the list of EC2 instance IDs
sorted_instance_ids = sorted(instance_ids)
print(f"Sorted EC2 Instance IDs: {sorted_instance_ids}")

# Length of a list
# Get the number of IP addresses in the security group  
num_ip_addresses = len(ip_addresses)
print(f"Number of IP addresses in the security group: {num_ip_addresses}")

# Accessing elements in a list of availability zones
# Access the first availability zone
first_az = availability_zones[0]
last_az = availability_zones[-1]
print(f"First Availability Zone: {first_az}")
print(f"Last Availability Zone: {last_az}")