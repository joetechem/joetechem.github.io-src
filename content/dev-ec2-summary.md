Title: EC2 Summary   
Author: Joe Seiler  
Date: 2018-12-27   
Category: Amazon   
Tags: aws, ec2, developer, cloud  
Slug: ec2-summary  

# EC2 - Summary/Exam Tips  

https://aws.amazon.com/ec2/  

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html  

* Know differences between;  
    - On-Demand  
    - Spot  
    - Reserved  
    - Dedicated Hosts  

* Remember with spot instances;  
    - If you terminate the instance, you pay for the hour  
    - If AWS terminates the spot instance (becasue spot price went above bid price), you get the hour it was terminated in for free.  

***  

## EC2 - Instance Types *DrMcGIFTPX*  

| Family  | Specialty                     |  Use Case                           |
|---------|-------------------------------| ----------------------------------  |
| D2      | Dense Storage                 | Filservers/Data Warehousing/Hadoop  |
| R4      | Memory Optimized              | Memory Intensive Apps/DBs           |
| M4      | General Purpose               | Application Servers                 |
| C4      | Compute Optimized             | CPU Intensive Apps/DBs              |
| G2      | Graphics Intensive            | Video Encoding/3D App Streaming     |
| I2      | High Speed Storage            | NoSQL DBs, Data Warehousing etc     |
| F1      | Field Programmable Gate Array | Hardware acceleration for your code |
| T2      | Lowest Cost, General Purpose  | Web Servers/Small DBs               |
| P2      | Graphics/General Purpose GPU  | Machine Learning, Bit Coin Mining   | 
| X1      | Memory Optimized              | SAP HANA/Apache Spark etc           |  

***  

* EBS Consists of:  
    - SSD, General Purpose - GP2 (Up to 10,000 IOPS)  
    - SSD, Provisioned IOPS - IO1 (More than 10,000 IOPS)  
    - HDD, Throuput Optimized - ST1 - Frequently accessed workloads (can't be used as boot volumes, can only be additional attached volume to an EC2 instance)  
    - HDD, Cold - SC1 - less frequently accessed data (can't be used as boot volumes, can only be additional attached volume to an EC2 instance)  
    - HDD, Magnetic - Standard - cheap, infrequently accessed storage (can have this as boot volume)  

* **You cannot mount 1 EBS volume to multiple EC2 instances, instead use EFS**    


* Termination Protection is turned off by default, you must turn it on.  
* On an EBS-Backed instance, the default action is for the root EBS volume to be deleted when the instance is terminated.  
* Root Volumes cannot be encrypted by default, you need a third party tool (such as bit locker etc) to encrypt the root volume  
* Additional volumes can be encrypted  

***  

## Volumes & Snapshots  

* Volumes exist on EBS  
    - Virtual Hard Disk  

* Snapshots exist on S3
    - You can take a snapshot of a volume, this will store that volume on S3.  
    - Snapshots are point-in-time copies of Volumes  
    - Snapshots are incremental, this means that only the blocks that have changed since your last snapshot are moved to S3.  
    - The first snapshot takes some time to create, additional snapshots afterwards are created faster  

## Volumes vs Snapshot - Security  

* Snapshots of encrypted volumes are encrypted automatically.  
* Volumes restored from encrypted snapshots are encrypted automatically.  
* You can share snapshots, but only if the are unencrypted.  
    - These snpashots can be shared with other AWS accounts or you can make them public in the Amazon Marketplace  

## Snapshots of Root Device Volumes  
* To create a snapshot for Amazon EBS volumes that serve as root devices, you should stop the instance before taking the snapshot  

## EBS vs Instance Store  

#### How can I take a Snapshot of a RAID Array?  
* Problem - Take a snapshot, the snapshot excludes data held in the cache by applications and the OS. This tends to not matter on a single volumes; however, using multiple volumes in a RAID array, this can be a problem due to interdependencies of the array.  

* Solution - Take an application consistent snapshot  
    - Stop the application from writing to disk  
    - Flush all caches to the disk.  
    - How can we do this?  
        - Freeze the file system  
        - Unmount the RAID Array  
        - Shutting down the associated EC2 instance  
        - Then take the snapshot  
        - *essentially, **you are trying to stop any kind of I/O being read from that RAID Array*** 

## CloudWatch  

* Standard Monitoring = 5 Min  
* Detailed Monitoring = 1 Minute  

* CloudWatch is for performance monitoring  
* CloudTrail is for auditing  

### What can I do with CloudWatch?  
* **Dashboards** - creates awesome dashboards to see what is happening with your AWS environment  
* **Alarms** = Allows you to set Alarms that notify you when particular thresholds are hit.  
* **Events** - CloudWatch Events helps you to respond to state changes in your AWS resources  
* **Logs** - CloudWatch Logs helps you to aggregate, monitor, and store logs.  

## IAM Roles  
* Roles are more secure than storing your access key and secret access key on individual EC2 instances.  
* Roles are easier to manage from a security perspective  
* Roles can be assigned to an EC2 instance AFTER it has been provisioned using both the command line and the AWS console. -takes effect immediately  
    - can also change the role's policies at any time -also takes effect immediately  
* Roles are universal, you can use them in any Region  

## Instance Met-data  
* Use to get info about an instance (such as public ip)  
* `curl http://169.256.169.256/latest/meta-data/`  

## EFS Features  
* Supports the Network File System 4 (NFSv4) protocol  
* You only pay for the storage you use (no pre-provisioning required)  
* Can scale up to the PETABYTES  
* Can support thousands of concurrent NFS connection  
* Data is stored across multiple AZ's within a region  
* Read After Write Consistency  

## Lambda  
* A compute service where you can upload your code and create a Lambda Function.  
* AWS takes care of the provisioning and managing the servers that you use to run the code.  
* Don't have to worry about OS's, patching, scaling, etc.  
* You can use Lambda ins the following ways:  
    - As an event-driven compute service where AWS Lambda runs your code in response to events. These events could be changes to data in an AMazon S3 bucket or an Amazon DynamoDB table.  
    - As a compute service to run your code in response to HTTP requests using Amazon API Gateway or API calls made using AWS SDKs. This is what A Cloud Guru does.  

## ECS - Elastic Container Service  

* The Elastic Container Service is a service that manages running Docker containers on a group of your EC2 instances.  