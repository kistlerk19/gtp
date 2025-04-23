# Stage 1: Build the application
FROM node:16-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY . .

# Stage 2: Create the runtime image
FROM node:16-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/server.js .
COPY --from=builder /app/package*.json .
EXPOSE 3000
CMD ["npm", "start"]