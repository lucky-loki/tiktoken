
SPLIT_LINE := "\033[44;32m >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \033[0m "

# proto
API_PROTO_FILES=$(shell find api -name *.proto)

.PHONY: api
api:
	@echo  $(SPLIT_LINE)"\033[33m$@\033[0m"
	python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. $(API_PROTO_FILES)


.PHONY: sdk
sdk:
	protoc --proto_path=api \
 	       --go_out=paths=source_relative:sdk \
 	       --go-grpc_out=paths=source_relative:sdk \
	       $(API_PROTO_FILES)
