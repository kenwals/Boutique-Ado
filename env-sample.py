import os

os.environ.setdefault("STRIPE_PUBLIC_KEY", "secret")
os.environ.setdefault("STRIPE_SECRET_KEY", "secret")
os.environ.setdefault("STRIPE_WH_SECRET", "secret")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "secret")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "secret")
os.environ.setdefault("DATABASE_URL", "secret")
os.environ.setdefault("EMAIL_HOST_PASS", "secret")
os.environ.setdefault("EMAIL_HOST_USER", "secret")
os.environ.setdefault("USE_AWS", "secret")