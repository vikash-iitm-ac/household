# Use Node.js as base image
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy app files and build the Vue app
COPY . .
RUN npm run build

# Serve the VueJS app using a lightweight web server
EXPOSE 8080
CMD ["npm", "run", "serve"]

