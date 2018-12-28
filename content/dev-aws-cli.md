Title: AWS CLI  
Author: Joe Seiler  
Date: 2018-12-27   
Category: Amazon     
Tags: aws, ec2, developer, cloud, cli  

# AWS CLI - Using IAM User Credentials  

[AWS - Configure CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)  

[AWS - CLI Profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-multiple-profiles.html)  

## Firing Up AWS CLI  

#### Configure AWS Credentials    
*Use the credentials of the aws account that has proper aws services access for what you are doing.*  
Get the credentials from the `.csv` file you save and put somewhere safe when you first created the aws user account (either through IAM user, or your root aws account)  
*while in root:*  
```bash  
aws configure
AWS Access Key ID [None]: access key ID here  
AWS Secret Access Key [None]: secret access key here
Default region name [None]: your region
Default output format [None]:
```  

#### Test an AWS CLI command:  
```bash  
aws s3 ls
```  

Above command will show you all your buckets from around the world (because S3 is a global service)  

#### Get list of AWS CLI commands for particular service:  
```bash  
aws s3 help
```  

#### See where the credentials are being stored:  
```bash  
cd ~
ls
cd .aws
ls
nano credentials
```  

Because these credentials could potentially be "hacked", it is MORE SECURE to use IAM Roles instead of using your root account for provisioning, deploying, and documenting (i.e. GitHub).  

## Self Destruct EC2 Instance from AWS CLI  

#### get EC2 instance's ID  
```bash  
aws ec2 describe-instances
```  
Locate the Instance ID of the one you want terminated.  

```bash  
aws ec2 terminate-instances --instance-ids i-0a6888aa0caabd8f3
```  

***  

**Having User credentials stored on an EC2 instance is a HUGE security risk.**  

Do not use IAM Users for the command line wherever possible, but if you are using it on your laptop, desktop or anything outside of AWS, then you will need a User with programmatic access.  

So, if you accidently upload your code to GitHub that has your Access Key ID and Secret Access Key, the best (only) way to resolve the issue is to delete the User and create a new one, or regenerate the credentials.  

Use IAM Roles over IAM Users wherever possible.  

***  

# AWS CLI - Using Roles  
## Identity Access Management Roles  

[AWS Switching Roles using CLI](https://aws.amazon.com/blogs/security/new-attach-an-aws-iam-role-to-an-existing-amazon-ec2-instance-by-using-the-aws-cli/)  

[AWS Switching Roles using Console](https://aws.amazon.com/blogs/security/easily-replace-or-attach-an-iam-role-to-an-existing-ec2-instance-by-using-the-ec2-console/)

If you used an IAM User account to provision a cluster of EC2 instances, and someone gained access to the User credentials for one of them, you would have to change the credentials for every other EC2 instance. This is an administrated BURDEN!  

**IAM Roles are global, it does not matter which you Region you create it in, it will be avilable across all Regions.**  

**It is possible to attach a Role to running EC2 instance**  

## IAM/S3 Lab  

* Create a new IAM Role with S3 Full Access  
* Launch an EC2 instance with the S3 Full Access role attached  
* SSH into the new instance  

#### See contents of S3  
```bash  
aws s3 ls
```  
This command works straight away, because the IAM Role with full S3 admin access is attached to this instance, giving it the permissions it needs to access S3.  

You can test by following steps above to find the secret directory with the credentials (it isn't there).  

* When using an IAM Role  
    - Don't need to store your credentials locally
    - if your credentials change, you don't need to login into your EC2 instances and update them  

* If you don't provision the EC2 instance with the IAM Role not attached,  
    - You can attach a Role to an EC2 instance while it is running
        - via the CLI or AWS Console  

***  

# CLI Commands - Developer Associate Exam - lab  

* Create new IAM Role:  
    - Service = EC2  
    - Permissions = Admin Access  
* Create new EC2 Instance with IAM Role attached  

#### Provision an EC2 Instance from the CLI:  
```bash  
aws configure  
# leave access key ID and secret access blank  
# Use the Region you are in for the Default region name
# leave output format blank
```  

## 3 Specific Commands for the Developer Associate Exam  

[AWS CLI Command Reference](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Instances:)  

You don't need to memorize any commands, just need to recognize the language they use.  

**Four important commands to remember:**  
1. Describe instances you currently have running  
    - `aws ec2 describe-instances`  
2. Describe instances available to you, that you can provision instances from  
    - `aws ec2 describe-images`  
3. Create an instance  
    - `aws ec2 run-instances`  

     *Don't confuse start-instances with run-instances*  
4. Terminate an instance  
    - `aws ec2 terminate-instances`  

**Example**  
#### To launch an instance in EC2-VPC:  
*The key pair named `MyKeyPair` and the security group `sg-903004f8` must exist.  
```bash  
aws ec2 run-instances --image-id ami-abc12345 --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-1a2b3c4d --subnet-id subnet-6e7f829e
```  

#### Terminate Instance Command  
[terminate-instance](https://docs.aws.amazon.com/cli/latest/reference/ec2/terminate-instances.html)  
```bash  
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```  

***  

# Bash Scripting  

**Bash Script:** a list of AWS command lines that will be run after an instance EC2 launches.  

**Good idea to create your bash script while trying out the commands in a test instance**  

* created *index.html*  
* created new S3 bucket, *mysimplebashbucket*  

**All S3 buckets are private by default**  
* Create new IAM Role:  
    - Service = EC2  
    - Permissions = Admin Access  

* started *simplebashscript.txt*  
    ```bash  
    #!/bin/bash
    yum update -y
    ```  

* created EC2 instance with new IAM Role attached  
    - SSH into instance  
    - `yum install httpd -y` to install Apache  
        - update bash txt with new commands  
    - `service httpd start` start the Apache service  
    - `chkconfig httpd on` make sure service automatically starts in case instance reboots  
    - `aws s3 ls` check contents of S3 (also good to check the correct Role/Permissions are attached)
    - `aws s3 cp s3://mysimplebashbucket/index.html /var/www/html` copy from s3 bucket to /var/www/html directory  

# Install PHP and Composer  

## Lab - Setting Up the PHP SDK  

#### bash script for S3  
```bash  
#!/bin/bash
yum update -y
yum install httpd24 php56 git -y
service httpd start
chkconfig httpd on
cd /var/www/html
echo "<?php phpinfo();?>" > test.php
git clone https://github.com/acloudguru/s3
```  

Type in the instance's `publicIPaddress/test.php` into browser, to check if the script worked.  

From https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started_installation.html insert the commands to install AWS SDK for PHP version 3:  

#### while in root, /var/www/html  
```bash  
curl -sS https://getcomposer.org/installer | php
php composer.phar require aws/aws-sdk-php
```  

Everytime you are using a PHP script to use the SDK, you need to run the `autoload.php` first  
#### autoload.php contents:  
```php  
<?php

// autoload.php @generated by Composer

require_once __DIR__ . '/composer/autoload_real.php';

return ComposerAutoloaderInit3b67dfc3d40d2cd9089a5411e8f40636::getLoader();
```  

## Lab - Interacting with S3 using the PHP SDK  

#### While logged in as root in the same instance as above:  
```bash  
cd /var/www/html/s3
ls
nano createbucket.php
```  

What happens:  
* Type instance's `publicIPaddress/createbucket.php` in browser  
    - a new bucket is created in S3  
    - click the link that comes up on each page  
        - first link, uploads a simple text file  
        - second link, to read the file  
        - third link, deletes the file object from the bucket  
        - fourth link, deletes the bucket if it is empty (and it is)  

# EC2 Instance Metadata  

How to get an instance's matadata while logged into it.  

[aws source](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)  

#### IP Address to remember for the exam:  
```bash  
curl http://169.254.169.254/latest/meta-data/  
```  

#### Get instance's public IP address:  
```bash  
curl http://169.254.169.254/latest/meta-data/public-ipv4
```  

**Returns META DATA, not user data!**  
**Use IP address, 169.254.169.254**    

