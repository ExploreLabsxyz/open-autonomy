<a name="autonomy.analyse.abci.docstrings"></a>
# autonomy.analyse.abci.docstrings

Analyse ABCI app definitions for docstrings.

<a name="autonomy.analyse.abci.docstrings.docstring_abci_app"></a>
#### docstring`_`abci`_`app

```python
docstring_abci_app(abci_app: Any) -> str
```

Generate a docstring for an ABCI app

This ensures that documentation aligns with the actual implementation

**Arguments**:

- `abci_app`: abci app object.

**Returns**:

docstring

<a name="autonomy.analyse.abci.docstrings.compare_docstring_content"></a>
#### compare`_`docstring`_`content

```python
compare_docstring_content(file_content: str, docstring: str, abci_app_name: str) -> Tuple[bool, str]
```

Update docstrings.

