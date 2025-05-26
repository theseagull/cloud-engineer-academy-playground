# def function_name(parameter1, parameter2):
# # Function bpdy eg, Code to be executed
#     return result # Optional

import random

def generate_bucket_name(project_name):
    random_suffix = random.randint(1000, 9999)
    bucket_name = f"{project_name}-bucket-{random_suffix}"
    return bucket_name

# Using the function
new_bucket_name = generate_bucket_name("myproject")
print(f"Generated S3 bucket name: {new_bucket_name}")