# SkillBridge — AI Adaptive Onboarding Engine
# Serves the single-file app via nginx on port 80

FROM nginx:alpine

# Copy the app
COPY adaptive-onboarding-engine.html /usr/share/nginx/html/index.html

# Optional: custom nginx config for proper MIME types and caching
RUN echo 'server { \
    listen 80; \
    root /usr/share/nginx/html; \
    index index.html; \
    location / { \
        try_files $uri $uri/ /index.html; \
        add_header Cache-Control "no-cache"; \
        add_header Access-Control-Allow-Origin "*"; \
    } \
}' > /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
