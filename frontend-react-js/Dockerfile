FROM node:16.18
LABEL vendor="Bootcamp"
LABEL built-by="josh"
WORKDIR /frontend-react
COPY . /frontend-react-js
RUN apt update && apt install -y curl && npm install -g npm@9.6.1
ENV PORT=3000
EXPOSE ${PORT}
CMD ["npm", "start"]