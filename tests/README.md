Using Pytest for CI/CD

### Unit Tests
```
PYTHONPATH=. pytest tests/unit -v
```

### Integration test

```
pytest tests/integration -v
pytest tests/integration_prod -v
```

Dev Verification
```
python  tests/integration/main.py
```
