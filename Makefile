
VERSION := 0.0.2
CR := 192.168.3.102:5000
NAME := palworld-exporter

build:
	docker build -t $(CR)/$(NAME):$(VERSION) .

push:
	docker push $(CR)/$(NAME):$(VERSION)

push-dockerhub:
	docker tag $(CR)/$(NAME):$(VERSION) mocchi/$(NAME):$(VERSION)
	docker tag $(CR)/$(NAME):$(VERSION) mocchi/$(NAME):latest
	docker push -a mocchi/$(NAME)

