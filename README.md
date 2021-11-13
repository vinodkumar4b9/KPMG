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

Attaching screen shots regarding the same 


![image](https://user-images.githubusercontent.com/12294021/141614853-a7551305-4c2e-45a5-ba32-b1d6b319130b.png)
![image](https://user-images.githubusercontent.com/12294021/141614872-71062231-b5a2-4abb-b96d-5b7d4cb5f2f7.png)
![image](https://user-images.githubusercontent.com/12294021/141614876-12e8f0b1-e2a1-43ca-b427-bd9010302ce0.png)

Pass the Required values in Parameterts and then click on Next and in End click on Create task 
![image](https://user-images.githubusercontent.com/12294021/141615000-606b6838-61ba-4cac-a59b-51eb1d278a25.png)



------------------------------------------------------------------------------------------------------------------------------------------------------------------
Task 2

Regarding Task 2 I have created a shell script(meta.sh) that will query the meta data of an instance within AWS in JSOM format, You can use the Simple shell script which fetches the data in JSON format as below 

![image](https://user-images.githubusercontent.com/12294021/141623019-041fee0b-da47-4656-b632-39bd9d56ef78.png)

if you want to fetch any specific value , you can parse that in Json query and get that for example in this case instance id as shown below 
![image](https://user-images.githubusercontent.com/12294021/141624305-ded7905e-42e9-4213-a872-b89bbe0d211d.png)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Regarding Task 3 , I have created a python script to get required output (nested-object.py) , You can run the command and will get required output , there are some prerequiste for this which was mentioned in Pythin script in inline comments , Please do read them before running the script

![image](https://user-images.githubusercontent.com/12294021/141651405-d179b7b3-bafe-44fc-95b9-b73a6ab44a19.png)




