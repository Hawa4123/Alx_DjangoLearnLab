
# -------------------------
# HTTPS & Security Settings
# -------------------------

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True  # Force HTTPS

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow domain to be included in browser preload lists

# Secure cookies
SESSION_COOKIE_SECURE = True  # Session cookies only sent over HTTPS
CSRF_COOKIE_SECURE = True     # CSRF cookies only sent over HTTPS

# Clickjacking protection
X_FRAME_OPTIONS = "DENY"  # Prevent framing of site

# Prevent MIME type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser XSS filter
SECURE_BROWSER_XSS_FILTER = True

# -------------------------
# Secure proxy SSL header (for deployments behind a proxy)
# -------------------------
# Tells Django that 'X-Forwarded-Proto' header should be trusted to determine HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
