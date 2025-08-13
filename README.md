# Password Holder

This project requires an encryption key for securing stored passwords.

Set the `ENCRYPTION_KEY` environment variable before running the application:

```bash
export ENCRYPTION_KEY=your-secret-key
python main.py
```

If the environment variable is not set, the application will prompt for the key using a secure input. If no key is provided, a `RuntimeError` is raised.
