FROM cgr.dev/chainguard/alpine-base
RUN apk update && apk upgrade --ignore alpine-baselayout
RUN printf "\nhttps://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk update && apk add pandoc npm && npm install --global mermaid-filter
RUN apk add jupyter-nbconvert chromium py3-airium

