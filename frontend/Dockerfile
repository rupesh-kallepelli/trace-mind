FROM node:20-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build


FROM nginx:stable-alpine

# ✅ Create all required dirs + fix permissions (OpenShift friendly)
RUN mkdir -p \
    /var/cache/nginx/client_temp \
    /var/cache/nginx/proxy_temp \
    /var/cache/nginx/fastcgi_temp \
    /var/cache/nginx/uwsgi_temp \
    /var/cache/nginx/scgi_temp \
    /var/run \
    && chgrp -R 0 /var/cache/nginx /var/run \
    && chmod -R g+rwX /var/cache/nginx /var/run

# ✅ Copy built app
COPY --from=build /app/dist /usr/share/nginx/html

# ✅ keep your existing config unchanged
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

# ✅ NO pid override anymore
CMD ["nginx", "-g", "daemon off;"]
