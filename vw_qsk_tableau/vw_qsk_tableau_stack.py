from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3
)

class VwQskTableauStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ami_image = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            #edition=ec2.AmazonLinuxEdition.STANDARD,
            #virtualization=ec2.AmazonLinuxVirt.HVM,
            #storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
            #cpu_type=ec2.AmazonLinuxCpuType.X86_64
        )

        instance_type = ec2.InstanceType('t2.micro')

        vpc = ec2.Vpc.from_lookup(self, "vpc",
            vpc_id = 'vpc-2250514b',
            # This imports the default VPC but you can also
            # specify a 'vpcName' or 'tags'.
            is_default=True
        )

        #vpc = ec2.Vpc(self, "VPC")

        # Example automatically generated from non-compiling source. May contain errors.
        sg = ec2.SecurityGroup.from_lookup_by_id(self, "SecurityGroupLookup", "sg-293e8d41")

        #rootVolume = ec2.BlockDevice(device_name="/dev/xvda",volume=ec2.BlockDeviceVolume.ebs(100))

        # AWS Linux 2
        instance = ec2.Instance(self, "VW_QSK_EC2",
            vpc=vpc,
            security_group=sg,
            instance_type=instance_type,
            #block_devices=[rootVolume],
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            )
        )

        instance.user_data.for_linux()
        instance.user_data.add_commands("wget https://downloads.tableau.com/esdalt/2022.3.0/tableau-server-2022-3-0.x86_64.rpm -O /tmp/tableau-install.rpm")
        #instance.user_data.add_s3_download_command(
        #    bucket=s3.Bucket(self, "vw-qsk-tableau-files"),
        #    bucket_key='registration.json'
        #)

        #useradd ${TsmUsername} && echo "Creating TSM user"
        #echo ${TsmPassword} | passwd ${TsmUsername} --stdin && echo "Setting password for TSM user"

        #/tmp/automated-installer -a tsadmin -s /tmp/secrets.txt -f /tmp/config.json -r /tmp/registration.json --accepteula --force tableau-install.rpm