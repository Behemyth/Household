terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0.0"
    }
  }
}

provider "azurerm" {}

resource "azurerm_resource_group" "homelab" {
  name     = "homelab-rg"
  location = "East US"
}
