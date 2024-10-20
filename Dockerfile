FROM alpine:latest
RUN apk add --no-cache ca-certificates
COPY node_exporter-1.8.2.linux-amd64/node_exporter /usr/local/bin/node_exporter
EXPOSE 9100
ENTRYPOINT ["/usr/local/bin/node_exporter"]
