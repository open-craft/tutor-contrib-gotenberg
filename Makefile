.DEFAULT_GOAL := help
.PHONY: docs
SRC_DIRS = ./src/tutorgotenberg
CMD_PREFIX ?= uv run

# Warning: These checks are not necessarily run on every PR.
test: test-lint test-types test-format  # Run some static checks.

test-format: ## Run code formatting tests
	$(CMD_PREFIX) ruff format --check --diff

test-lint: ## Run code linting tests
	$(CMD_PREFIX) ruff check

test-types: ## Run type checks.
	$(CMD_PREFIX) ty check

format: ## Format code automatically
	$(CMD_PREFIX) ruff format

ESCAPE = 
help: ## Print this help
	@grep -E '^([a-zA-Z_-]+:.*?## .*|######* .+)$$' Makefile \
		| sed 's/######* \(.*\)/@               $(ESCAPE)[1;31m\1$(ESCAPE)[0m/g' | tr '@' '\n' \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-30s\033[0m %s\n", $$1, $$2}'
