FROM node:16.18
LABEL vendor="Bootcamp"
LABEL built-by="josh"
RUN apt update && apt install -y curl && npm install -g npm@9.6.1
COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
ENV PORT=3000
EXPOSE ${PORT}
CMD ["npm", "start"]