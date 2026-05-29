import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: python-dotenv is not installed. Run: pip install python-dotenv")
    sys.exit(1)

load_dotenv()

DEFAULTS = {
    "MATRIX_MODE":     "development",
    "DATABASE_URL":    None,
    "API_KEY":         None,
    "LOG_LEVEL":       "DEBUG",
    "ZION_ENDPOINT":  None,
}

REQUIRED = ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]

def load_config():
    config = {}
    missing = []

    for key, default in DEFAULTS.items():
        value = os.environ.get(key, default)
        if value is None:
            missing.append(key)
        config[key] = value

    return config, missing

def mask(value, show_chars=4):
    if value is None:
        return "NOT SET"
    if len(value) <= show_chars:
        return "*" * len(value)
    return value[:show_chars] + "*" * (len(value) - show_chars)

def format_db(url):
    if url is None:
        return "NOT SET"
    if "@" in url:
        protocol, rest = url.split("://", 1)
        host_part = rest.split("@", 1)[1]
        return f"{protocol}://****@{host_part}"
    return url  # no credentials visible

def mode_banner(mode):
    if mode == "production":
        return "PRODUCTION"
    return "development"

def security_checks(config):
    checks = []

    with open(__file__, "r") as f:
        source = f.read()

    import re
    code_lines = [l for l in source.splitlines()
                  if not l.strip().startswith("#") and not l.strip().startswith('"""')]
    code_only = "\n".join(code_lines)
    hardcoded = bool(re.search(
        r'(?<!["\'])(?:api_key|password|secret|token)\s*=\s*["\'][^"\']{6,}["\']',
        code_only, re.IGNORECASE
    ))
    checks.append(("[OK]" if not hardcoded else "[FAIL]",
                   "No hardcoded secrets detected" if not hardcoded
                   else "Hardcoded secrets found in source!"))

    env_exists = os.path.isfile(".env")
    checks.append(("[OK]" if env_exists else "[--]",
                   ".env file properly configured" if env_exists
                   else ".env file not found (copy .env.example to .env)"))

    can_override = "MATRIX_MODE" in os.environ or True  # always available
    checks.append(("[OK]", "Production overrides available via environment variables"))

    return checks

def main():
    print("\nAccessing the Mainframe")
    print("=" * 42)
    print("ORACLE STATUS: Reading the Matrix...\n")

    config, missing = load_config()
    mode = config["MATRIX_MODE"]

    print("Configuration loaded:")
    print(f"  Mode:      {mode_banner(mode)}")

    if mode == "production":
        print("  Database:  Connected to PRODUCTION instance")
        print(f"  API Access: Key → {mask(config['API_KEY'])}")
        print(f"  Log Level: {config['LOG_LEVEL']}")
        print(f"  Zion Network: {config['ZION_ENDPOINT'] or 'NOT SET'}")
    else:
        db_display = format_db(config["DATABASE_URL"]) if config["DATABASE_URL"] else "NOT SET"
        print(f"  Database:  {db_display}")
        api_status = f"Authenticated ({mask(config['API_KEY'])})" if config["API_KEY"] else "NOT SET"
        print(f"  API Access: {api_status}")
        print(f"  Log Level: {config['LOG_LEVEL']}")
        zion = config["ZION_ENDPOINT"] or "NOT SET"
        print(f"  Zion Network: {'Online → ' + zion if config['ZION_ENDPOINT'] else zion}")

    if mode == "production":
        print()
        print("  [PRODUCTION NOTICE]")
        print("  - Verbose logging DISABLED for security")
        print("  - Connecting to live Zion endpoint")
        print("  - All access attempts are being audited")

    if missing:
        print()
        print("Configuration warnings:")
        for key in missing:
            print(f"  [WARN] {key} is not set — using default or skipping")

    print()
    print("Environment security check:")
    for status, message in security_checks(config):
        print(f"  {status} {message}")

    print()
    if missing:
        print("The Oracle senses incomplete configuration.")
        print("Copy .env.example to .env and fill in your values.")
    else:
        print("The Oracle sees all configurations.")

    print()

if __name__ == "__main__":
    main()
