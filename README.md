# CICD with GitOps Project

## CI
Use a prober Git Branch Strategy
Don't edit directly on the main branch, Add a feature/new branch
when pushing into the featuer/* branches, the CI will git triggered and execute the following
	1- code
	2- build
	3- test
	4- package
	5- docker file
	6- docker build 
	7- docker push (Docker Hub or ECR)
	8- Change Manifests Image Tag

## Manual PR Merge into ./main
## CD
	8- ArgoCD detects changes from ./main
	9- Applies Manifests