# Use an official Node.js runtime as the base image
FROM node:14

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install Angular CLI globally
RUN npm install -g @angular/cli

# Install project dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Expose the default port used by ng serve
EXPOSE 4200

# Start the Angular development server with ng serve
CMD ["ng", "serve", "--host", "0.0.0.0"]