A highly available, scalable LAMP stack with an Amazon RDS database instance for the backend data store , You can find the template in YAML file which is 
there in this repository


This template demonstrates using the AWS CloudFormation bootstrap scripts to install the packages and files necessary to deploy the Apache web server and PHP at instance
launch time


Note: In the template I have mentioned , I will explain the steps briefly and stages and you can use the template in any region. As mentioned in document main purpose  of this yaml  is focused on the steps that are needed to setup a three tier  not the final output , Taking that into consideration I have made the template. Please find the details below 

---------------------------------------

Parameters : To Start with I will be defining the parameters which are needed to pass while building this cloudformation , here in this case we are passing VPC ID , Subnets , Keyname , DB name , DB user, DB storage class , Instance type and some additinal details needed

Mappings: After that we are using mappings The optional Mappings section matches a key to a corresponding set of named values. For example, if you want to set values based on a region, you can create a mapping that uses the region name as a key and contains the values you want to specify for each specific region.

Resources: After that we are creating resources which are needed , In this case we are creating Application Loadbalancer , Autoscaling group , Launch configuration for that ASG where we will be installing required packages , Instances , Security groups , And RDS DB. So In the Launch configuration we are installing all required packages so that As a part of ASG when new instances launches it will come with all pre installed software needed.

Ouputs: Once All the resources are created , In the outputs section we are getting Application Load balancer URL through which we can launch the lamp stack 
