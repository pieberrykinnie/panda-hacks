# Terraform configuration for StudyStreak infrastructure
terraform {
  required_version = ">= 1.0"
  required_providers {
    supabase = {
      source  = "supabase/supabase"
      version = "~> 0.1"
    }
  }
}

# Supabase project configuration
resource "supabase_project" "studystreak" {
  name        = "studystreak"
  organization_id = var.supabase_org_id
  region      = "us-east-1"
  plan        = "free"
}

# Environment variables for the API service
resource "supabase_project_secret" "openai_key" {
  project_id = supabase_project.studystreak.id
  name       = "OPENAI_API_KEY"
  value      = var.openai_api_key
}

# Output the database URL and API keys
output "supabase_url" {
  value = supabase_project.studystreak.api_url
}

output "supabase_anon_key" {
  value = supabase_project.studystreak.anon_key
  sensitive = true
}

output "supabase_service_key" {
  value = supabase_project.studystreak.service_role_key
  sensitive = true
}