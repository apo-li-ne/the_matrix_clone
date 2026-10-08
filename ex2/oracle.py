import os


from dotenv import load_dotenv

def main() -> None:
    load_dotenv()

    mode = os.getenv("MATRIX_MODE", "development")
    database = os.getenv("DATABASE_URL", "")
    api_key = os.getenv("API_KEY", "")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion = os.getenv("ZION_ENDPOINT", "")

    print("ORACLE STSATUS: Reading the Matrix...\n")

    if database == "" or api_key == "" or zion == "":
        print("WARNING: some configuration is missing.")
        print("Copy .env.example to .env and fill in the values.\n")

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if mode == "production":
        print("Database: Connected to production instance")
    else:
        print("Database: Conneceted to local instance")

    if api_key == "":
        print("API Access: No Key")
    else:
        print("API Access: Authenticated")

    print(f"Log Level: {log_level}")

    if zion == "":
        print("Zion Network: Offline")
    else:
        print("Zion Network: Online")

    print("\nEnvironment security check:")
    if os.path.exists(".gitignore"):
        print("[OK] .gitignore found")
    else:
        print("[WARNING] .gitignore missing")

    print("\nThe Oracle sees all configurations")

if __name__ == "__main__":
    main()