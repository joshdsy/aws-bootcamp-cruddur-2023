FROM node:16.18
LABEL vendor="Bootcamp"
LABEL built-by="josh"
ENV PORT=3000
COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN apt update && apt install -y curl
RUN npm install
EXPOSE ${PORT}
CMD ["npm", "start"]