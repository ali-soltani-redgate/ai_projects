# Tips

## Virtual env and Python interpreter

- `uv` always uses the project's own `.venv` regardless of what's activated in terminal
- VS Code won't auto-discover `.venv` in deeply nested folders — use "Enter interpreter path" and browse to `customer_profiler/api/.venv/Scripts/python.exe`
- Activated shell env doesn't affect `uv add` / `uv run` — they always target the current project's `.venv`

## Add packages with UV with right structure

- Run `uv init <project_name> --package` to get a src layout automatically
- Run `uv add <package>` from the folder containing `pyproject.toml` — it adds to deps AND installs
- No need to manually `uv sync` after `uv add`
- Use `uv run <command>` to run tools using the project's venv without activating it

## API

### Check health with curl

```bash
curl http://localhost:8000/api/v1/health
```

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- Run server: `uv run uvicorn api.main:app --reload` (from the `api/` folder)