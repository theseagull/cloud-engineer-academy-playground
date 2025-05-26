# Define the AWS account ID
aws_account_id = '123456789012'

# Define the project name
project_name = 'cloud_project'

# Concatenate strings to form the S3 bucket name
s3_bucket_name = aws_account_id + '-' + project_name + '-bucket'

# Print the S3 bucket name
print(f"S3 Bucket Name: {s3_bucket_name}")

# Exercise

# Environment name prod, dev, staging
environment = 'dev'

# Application name
application = 'appserver'

# Instance number
instance_number = "02"

# Instance name
instance_name = environment + '-' + application + '-instance-' + instance_number

# Print the instance name
print(f"EC2 Instance Name: {instance_name}")