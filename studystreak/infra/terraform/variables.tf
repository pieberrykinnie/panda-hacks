# Terraform variables for StudyStreak infrastructure

variable "supabase_org_id" {
  description = "Supabase organization ID"
  type        = string
}

variable "openai_api_key" {
  description = "OpenAI API key for the agent service"
  type        = string
  sensitive   = true
}

variable "fly_api_token" {
  description = "Fly.io API token for deployment"
  type        = string
  sensitive   = true
}