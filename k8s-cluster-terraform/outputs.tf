output "kube_control_plane_ip" {
  value = aws_instance.kube_control_plane.private_ip
}

output "kube_node1_ip" {
  value = aws_instance.kube_node1.private_ip
}

output "kube_node2_ip" {
  value = aws_instance.kube_node2.private_ip
}

