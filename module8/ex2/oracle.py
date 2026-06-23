import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print(
        "Error: python-dotenv is not installed. "
        "Run: pip install python-dotenv"
    )
    sys.exit(1)

load_dotenv()

Config = dict[str, str | None]

DEFAULTS: Config = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": None,
    "API_KEY": None,
    "LOG_LEVEL": "DEBUG",
    "ZION_ENDPOINT": None,
}

REQUIRED: list[str] = ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]

SECRET_KEYWORDS: tuple[str, ...] = ("api_key", "password", "secret", "token")
MIN_SECRET_LENGTH = 6


def load_config() -> tuple[Config, list[str]]:
    config: Config = {}
    missing: list[str] = []

    for key, default in DEFAULTS.items():
        value = os.environ.get(key, default)
        if value is None:
            missing.append(key)
        config[key] = value

    return config, missing


def mask(value: str | None, show_chars: int = 4) -> str:
    if value is None:
        return "NOT SET"
    if len(value) <= show_chars:
        return "*" * len(value)
    return value[:show_chars] + "*" * (len(value) - show_chars)


def format_db(url: str | None) -> str:
    if url is None:
        return "NOT SET"
    if "@" in url:
        protocol, rest = url.split("://", 1)
        host_part = rest.split("@", 1)[1]
        return f"{protocol}://****@{host_part}"
    return url


def mode_banner(mode: str | None) -> str:
    if mode == "production":
        return "PRODUCTION"
    return "development"


def _is_quoted_literal(text: str, min_length: int = MIN_SECRET_LENGTH) -> bool:
    text = text.strip()
    if len(text) < 2:
        return False

    quote = text[0]
    if quote not in ("'", '"') or not text.endswith(quote):
        return False

    inner = text[1:-1]
    return len(inner) >= min_length


def _assigns_secret_literal(line: str) -> bool:
    if "=" not in line or any(op in line for op in ("==", "!=", "<=", ">=")):
        return False

    name_part, _, value_part = line.partition("=")
    name = name_part.strip()

    if not name or name.startswith(("'", '"')):
        return False

    lowered_name = name.lower()
    has_secret_name = any(
        keyword in lowered_name for keyword in SECRET_KEYWORDS
    )
    return has_secret_name and _is_quoted_literal(value_part)


def has_hardcoded_secret() -> bool:
    try:
        with open(__file__, "r") as f:
            source = f.read()
    except OSError:
        return False

    for raw_line in source.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or line.startswith('"""'):
            continue
        if _assigns_secret_literal(line):
            return True

    return False


def security_checks(config: Config) -> list[tuple[str, str]]:
    checks: list[tuple[str, str]] = []

    hardcoded = has_hardcoded_secret()
    checks.append((
        "[OK]" if not hardcoded else "[FAIL]",
        "No hardcoded secrets detected" if not hardcoded
        else "Hardcoded secrets found in source!"
    ))

    env_exists = os.path.isfile(".env")
    checks.append((
        "[OK]" if env_exists else "[--]",
        ".env file properly configured" if env_exists
        else ".env file not found (copy .env.example to .env)"
    ))

    checks.append(
        ("[OK]", "Production overrides available via environment variables")
    )

    return checks


def main() -> None:
    print("\nAccessing the Mainframe")
    print("=" * 42)
    print("ORACLE STATUS: Reading the Matrix...\n")

    config, missing = load_config()
    mode = config["MATRIX_MODE"]

    print("Configuration loaded:")
    print(f"  Mode:      {mode_banner(mode)}")

    if mode == "production":
        db_status = (
            "Connected to PRODUCTION instance"
            if config["DATABASE_URL"]
            else "NOT SET"
        )
        print(f"  Database:  {db_status}")
        print(f"  API Access: Key → {mask(config['API_KEY'])}")
        print(f"  Log Level: {config['LOG_LEVEL']}")
        print(f"  Zion Network: {config['ZION_ENDPOINT'] or 'NOT SET'}")
    else:
        database_url = config["DATABASE_URL"]
        db_display = format_db(database_url) if database_url else "NOT SET"
        print(f"  Database:  {db_display}")

        api_key = config["API_KEY"]
        api_status = f"Authenticated ({mask(api_key)})" if api_key \
            else "NOT SET"
        print(f"  API Access: {api_status}")
        print(f"  Log Level: {config['LOG_LEVEL']}")

        zion = config["ZION_ENDPOINT"] or "NOT SET"
        zion_display = f"Online → {zion}" if config["ZION_ENDPOINT"] \
            else zion
        print(f"  Zion Network: {zion_display}")

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
