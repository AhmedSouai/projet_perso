resource "aws_instance" "kube_control_plane" {
  ami             = "ami-xxxxxxxx"  # Remplace par l'AMI Ubuntu correcte
  instance_type   = var.instance_type
  key_name        = var.key_name
  private_ip      = "192.168.56.10"
  
  tags = {
    Name = "kube-control-plane"
  }
}

resource "aws_instance" "kube_node1" {
  ami             = "ami-xxxxxxxx"
  instance_type   = var.instance_type
  key_name        = var.key_name
  private_ip      = "192.168.56.11"

  tags = {
    Name = "kube-node1"
  }
}

resource "aws_instance" "kube_node2" {
  ami             = "ami-xxxxxxxx"
  instance_type   = var.instance_type
  key_name        = var.key_name
  private_ip      = "192.168.56.12"

  tags = {
    Name = "kube-node2"
  }
}
