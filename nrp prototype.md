###nrp prototype deployment to dev beanstalk

#### infrastructure 

1. create stack (dev AWS account)
`aws elasticbeanstalk create-application --application-name nrp-prototype`

2. create a dev environment in that stack (using Ethan's cloudformation templates, in particular the python 3.4 in docker template.  Thanks, Ethan!)
`./launch-stack-py34 nrp-prototype dev NRP`

3. review the cloudformation console for the elastic load balancer cname for this environment

```
Key	Value
AWSEBLoadBalancerURL	http://internal-awseb-e-b-AWSEBLoa-WIQBXBEELXJJ-399431783.us-east-1.elb.amazonaws.com
```

4. create a cname to the elb for friendly use

'''
nrp-prototype.dev.nrgpl.us  CNAME   internal-awseb-e-b-AWSEBLoa-WIQBXBEELXJJ-399431783.us-east-1.elb.amazonaws.com
'''

#### deployment
1. steal elb file and docker file from dev nrghomepower build
