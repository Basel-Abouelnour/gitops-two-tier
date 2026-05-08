FROM node:18-slim
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY backend.js .
EXPOSE 5000
CMD ["npm", "start"]