# Single quotes
single_quote = 'This is an EC2'

# Double quotes
double_quote = "This is an S3 bucket"

# Triple quotes for multi-line strings
multi_line = """
This is a CloudFormation template.
Which has multiple lines.
"""

print(single_quote)
print(double_quote)
print(multi_line)

# Exercise
# Create a single-quoted string for an AWS region name
aws_region = 'us-west-2'

# Create a double-quoted string for an EC2 instance type
ec2_instance_type = "t2.micro"

# Create a multi-line string for a simple IAM policy
iam_policy = """
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::example-bucket"
        }
    ]
}
"""

# Print all three strings
print(aws_region)
print(ec2_instance_type)
print(iam_policy)