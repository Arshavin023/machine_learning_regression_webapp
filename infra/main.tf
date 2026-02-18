provider "aws" {
  region = "us-east-1"
}

resource "aws_ecs_cluster" "ml_cluster" {
  name = "ml-cluster"
}

resource "aws_ecr_repository" "ml_repo" {
  name = "math-score-app"
}

resource "aws_ecs_task_definition" "ml_task" {
  family                   = "ml-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"

  container_definitions = jsonencode([
    {
      name      = "ml-container"
      image     = "${aws_ecr_repository.ml_repo.repository_url}:latest"
      essential = true
      portMappings = [
        {
          containerPort = 8000
          hostPort      = 8000
        }
      ]
    }
  ])
}
