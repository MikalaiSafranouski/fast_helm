

network: ## Create the slicelife network if it doesn't exist
	docker network create --driver bridge fast-network || true

build.base: ## Build the base service
	@docker-compose build base

build.test: ## Build the test container
	@docker-compose build test

start: network ## Run the application locally in the background
	@docker-compose up --build fast-web


stop: ## Stop the application
	@docker-compose down --remove-orphans


test: build.test network ## Run the unit tests and linters
	@docker-compose -f docker-compose.yaml -f env/test_env.yml run --rm test bash scripts/test.sh
ifeq ($(CI),true)
	@docker-compose -f docker-compose.yaml -f env/test_env.yml down --volumes
endif
