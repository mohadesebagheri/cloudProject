#!/bin/bash

main_yml_dir="./kubernetes_deployment/"
auth_yml_dir="auth-api/"

# Deploying mongodb

kubectl create secret generic postgres \
--from-literal=POSTGRES_USER="root" \
--from-literal=POSTGRES_PASSWORD="secret-password"

kubectl apply -f $main_yml_dir$auth_yml_dir"./webapp.yml"

kubectl apply -f $main_yml_dir$auth_yml_dir"./postgres-config.yml"

kubectl apply -f $main_yml_dir$auth_yml_dir"./postgres.yml"

kubectl apply -f $main_yml_dir$auth_yml_dir"./postgres-secret.yml"
