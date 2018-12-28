Title: EFS High Level  
Author: Joe Seiler  
Date: 2018-12-27   
Category: Amazon  
Tags: aws, ec2, efs, developer, cloud  
Slug: efs-high-level  

# EFS - Elastic File System  

Amazon Elastic File System (Amazon EFS) is a file storage service for Amazon EC2 instances. EFS provides a simple interface that allows you to create and configure file systems quickly and easily.  

## The "Elastic" in Elastic File System  
* Storage capacity is elastic, growing and shrinking automatically as you add and remove files  
    - so your applications have the storage they need, when they need it.  

<center>  

**You cannot mount an EBS volume to more than on EC2 instance at one time.**  
This is what EFS allows you to do  
**EFS allows multiple EC2 instances to connect to it**
Data is stored across multiple AZ's within a region.  
EFS is Block-Based storage (as opposed to Object-Based in S3)  
You can share files with between EC2 instances (EFS and EC2 instances must share the same Security Group to do this)  
Read after Write Consistency, like S3  

</center>  

## EFS Features  

* Supports the Network File System version 4 (NFSv4) protocol  
* You only pay for the storage you use (no pre-provisioning required)  
* Can scale up to the PETABYTES  
* Can support thousands of concurrent NFS connections  
* Data is stored across multiple Availability Zones within a Region  
* Share files between EC2 instances  
    - Ensure they the same Security Group assignment  
    - Ensure the Security Group has the NFS rule attached to it  

With EFS, a Load Balancer and EC2 instances provisioned with shared security groups and in the same AZ,  
you can have multiple EC2 instances accessing the same files.  

* You can also apply to EFS, user-level and directory-level permissions  
    - So you can make certain directories, or files restricted in EFS,  
        - this would be universal across all EC2 instances.  




