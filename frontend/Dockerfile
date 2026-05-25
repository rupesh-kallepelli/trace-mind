FROM node:20-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build


# ---- NGINX STAGE ----
FROM nginx:stable-alpine

# ✅ Create required temp directories
RUN mkdir -p \
    /var/cache/nginx/client_temp \
    /var/cache/nginx/proxy_temp \
    /var/cache/nginx/fastcgi_temp \
    /var/cache/nginx/uwsgi_temp \
    /var/cache/nginx/scgi_temp \
    /var/run \
    && chmod -R g+rwX /var/cache/nginx /var/run \
    && chgrp -R 0 /var/cache/nginx /var/run

# ✅ Copy app
COPY --from=build /app/dist /usr/share/nginx/html

# ✅ Keep your existing config (no change)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

# ✅ Override PID path at runtime (NO config change)
CMD ["nginx", "-g", "pid /var/run/nginx.pid; daemon off;"]
