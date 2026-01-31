# Stage 1: Build
FROM node:20-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm ci --no-audit  --no-fund
COPY . .
RUN npm run build -- --configuration=production

# Stage 2: Serve
FROM nginx:alpine
RUN  rm -rf /usr/share/nginx/html/*
COPY --from=build /app/dist/dashboard/ /usr/share/nginx/html/
RUN if [ -d "/usr/share/nginx/html/browser" ]; then \
    mv /usr/share/nginx/html/browser/* /usr/share/nginx/html/ && \
    rm -rf /usr/share/nginx/html/browser; \
    fi
RUN if [ -d "/usr/share/nginx/html/dashboard" ]; then \
    mv /usr/share/nginx/html/dashboard/* /usr/share/nginx/html/ && \
    rm -rf /usr/share/nginx/html/dashboard; \
    fi
RUN  rm -rf nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/nginx.conf /etc/nginx/conf.d/nginx.conf

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD wget --quiet --tries=1 --spider http://localhost || exit 1
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
