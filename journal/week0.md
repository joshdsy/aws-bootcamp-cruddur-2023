# Week 0 — Billing and Architecture

## Prerequisites
* GitHub Account
* Gitpod Account
* Github Codespaces Account 
* AWS Account
* Momento Account
* Custom Domain Name
* Lucid Charts
* HoneyComb.io
* Rollbar Account

1. Used my existing Github account and used [ExamProCo](https://github.com/ExamProCo/aws-bootcamp-cruddur-2023) repositry as a template.
2. Watched [Gifted Lane's Playlist](https://www.youtube.com/playlist?list=PL6RfZggzDojS8y2RYkvdLcvTd8ZpxEDoT) and opened accounts for [Gitpod](https://gitpod.io/) ,[Momento](https://www.gomomento.com/), [HoneyComb.io](https://www.honeycomb.io/) and [Rollbar](https://rollbar.com)
3. Created a New AWS account to be eligible fro the free tire.
4. Watched [Andrew Brown's video](https://www.youtube.com/watch?v=A6_c-hJmehs) on adding the Gitpod Button.
5. Bought a .link domain for Cohort: 2023-A1.



## Required Homework

1. Was unable to attend the complete Live session as it was very late in my time zone, watched remaining on [Youtube](https://www.youtube.com/watch?v=SG8blanhAOg&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=13) , Also watched [Generate Credentials, AWS CLI, Budget and Billing Alarm via CLI](https://www.youtube.com/watch?v=OdUnNuKylHg&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=15) from the same playlist.

2. Watched [Chirag's video](https://www.youtube.com/watch?v=OVw3RrlP-sI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=14) on Pricing basics and [Ashish's Week 0 - Security Considerations Video](https://www.youtube.com/watch?v=4EMWBYVggQI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=16)

 * Activated MFA for root user.

 ![image](../_docs/assets/week0/mfa.png)

3. Create Admin User(already created user for CLI)

4. Updated my `.gitpod.yml` to include the following:-

```sh
tasks:
  - name: aws-cli
    env:
      AWS_CLI_AUTO_PROMPT: on-partial
    init: |
      cd /workspace
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
      cd $THEIA_WORKSPACE_ROOT

```

added my ENV VARS to Gitpod under [variables](https://gitpod.io/user/variables)
* AWS_ACCESS_KEY_ID
* AWS_ACCOUNT_ID
* AWS_DEFAULT_REGION
* AWS_SECRET_ACCESS_KEY

or you can set them in the terminal

```
gp env AWS_ACCESS_KEY_ID=""
gp env AWS_SECRET_ACCESS_KEY=""
gp env AWS_DEFAULT_REGION=us-east-1
gp env AWS_ACCOUNT_ID=
```


Ran ``` aws sts get-caller-identity ```
to confirm my credentials were correct

5. Setup billing Alarms 

6. Created Conceptual Diagram Cruddur in Lucid Charts.
![image](../_docs/assets/week0/conceptualdiag.png)

7. Created Logical diagram for Cruddur in Lucid Charts
![image](../_docs/assets/week0/logicaldiag.png)

8. Used AWS Cloudshell 
```
[cloudshell-user@ip-10-12-46-255 ~]$ aws sts get-caller-identity 
{
    "UserId": "AIDAWIROA23Y65CPF3XUV",
    "Account": "430666995xxx",
    "Arn": "arn:aws:iam::430666995xxx:user/adminaccount"
}
[cloudshell-user@ip-10-12-46-255 ~]$ 

```

9. Create Budget

## Stretch Homework
1. Terraform billing alarms(to-do)
2. Use boto3 and python and create billing alarms(to-do)
3. Destroy your root account credentials, Set MFA, IAM role
4. Use EventBridge to hookup Health Dashboard to SNS and send notification when there is a service health issue
5. CI/CD logical pipeline in Lucid Charts 
![image](../_docs/assets/week0/cicd.png)
6. Reviewed he Six pillars of well architected framework.
  * ### Operational Excellence
  The operational excellence pillar focuses on running and monitoring systems, and continually improving processes and procedures. Key topics include automating changes, responding to events, and defining standards to manage daily operations.
  * ### Security
  The security pillar focuses on protecting information and systems. Key topics include confidentiality and integrity of data, managing user permissions, and establishing controls to detect security events.
  * ### Reliability
  The reliability pillar focuses on workloads performing their intended functions and how to recover quickly from failure to meet demands. Key topics include distributed system design, recovery planning, and adapting to changing requirements.
  * ### Performance Efficiency
  The performance efficiency pillar focuses on structured and streamlined allocation of IT and computing resources. Key topics include selecting resource types and sizes optimized for workload requirements, monitoring performance, and maintaining efficiency as business needs evolve.
  * ### Cost Optimization
  The cost optimization pillar focuses on avoiding unnecessary costs. Key topics include understanding spending over time and controlling fund allocation, selecting resources of the right type and quantity, and scaling to meet business needs without overspending.
  * ### Sustainability
  The sustainability pillar focuses on minimizing the environmental impacts of running cloud workloads. Key topics include a shared responsibility model for sustainability, understanding impact, and maximizing utilization to minimize required resources and reduce downstream impacts. 

  [Well Architected Map](https://wa.aws.amazon.com/wat.map.en.html)
## Blog posts

[dev.to---TODO](https://dev.to/joshdsy)