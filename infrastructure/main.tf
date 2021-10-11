terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.60.0"
    }
  }
}



provider "aws" {
  region  = "us-east-1"
  profile = "terraform-django-test"
}

data "aws_availability_zones" "available" {}

locals {
  public_subnets  = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
  private_subnets = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.7.0"

  name            = "django_test"
  cidr            = "10.0.0.0/16"
  azs             = data.aws_availability_zones.available.names
  public_subnets  = local.public_subnets
  private_subnets = local.private_subnets

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}


resource "aws_security_group" "rds" {
  name   = "django_test_rds"
  vpc_id = module.vpc.vpc_id

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = local.private_subnets
  }

  # sec groups are stateful, so i shouldnt need to define identical egress as long as the db doesnt try to connect the public instance by itself
  egress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = local.private_subnets
  }

  tags = {
    Name = "django_test_rds"
  }
}

resource "aws_db_subnet_group" "django_test_private" {
  name       = "django_test_private"
  subnet_ids = module.vpc.private_subnets

  tags = {
    Name = "django_test"
  }
}

resource "aws_db_parameter_group" "django_test_db_param_grp" {
  name   = "django-test-db-param-grp"
  family = "postgres12"

  parameter {
    name  = "log_connections"
    value = "1"
  }
}

resource "random_password" "django_rds_password" {
  length           = 16
  special          = true
  override_special = "_%@"
}

resource "random_password" "django_rds_username" {
  length  = 16
  special = false
  number  = false
}

resource "aws_db_instance" "django_test" {
  identifier             = "django-test"
  instance_class         = "db.t2.micro"
  allocated_storage      = 5
  engine                 = "postgres"
  engine_version         = "12.8"
  username               = random_password.django_rds_username.result
  password               = random_password.django_rds_password.result
  db_subnet_group_name   = aws_db_subnet_group.django_test_private.name
  vpc_security_group_ids = [aws_security_group.rds.id]
  parameter_group_name   = aws_db_parameter_group.django_test_db_param_grp.name
  publicly_accessible    = false
  skip_final_snapshot    = true
}


# module "ecs-fargate" {
#   source  = "cn-terraform/ecs-fargate/aws"
#   version = "2.0.27"
#   # insert the 25 required variables here
# }
