resource "aws_s3_bucket" "dL" {
  bucket = "datalake-igti-edac-william"
  acl    = "private"

  tags = {
    IES = "IGTI",
    CURSO = "EDAC"
  }
    
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}