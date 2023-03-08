FROM node:16-alpine
LABEL vendor="Bootcamp"
LABEL built-by="josh"
RUN apk add curl && npm install -g npm@9.5.1
COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
ENV PORT=3000
EXPOSE ${PORT}
CMD ["npm", "start"]