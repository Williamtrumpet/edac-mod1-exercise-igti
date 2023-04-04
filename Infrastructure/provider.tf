provider "aws" {
    region = var.aws_region
}

# Centralizar o arquivo de controle de estado do terraform
terraform {
  backend "s3" {
    bucket = "terraform-state-igti-will"
    key    = "state/igti/edc/terraform.tfstate"
    region = "us_east-2"
    
  }
}