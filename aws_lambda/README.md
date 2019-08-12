The lambda function, psycopg2 module, and a few helper functions are located inside the aws_deployment_package.zip file.

The lambda function will load Apple's, Google's, and Facebook's closing stock value into the AWS RDS database each day at 5:30 PM EST.

Important!

My deployment package uses a custom compiled psycopg2 module for psycopg2 to work. Link to a working library below:

https://github.com/jkehler/awslambda-psycopg2