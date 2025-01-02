<a name="autonomy.chain.metadata"></a>
# autonomy.chain.metadata

Metadata helpers.

<a name="autonomy.chain.metadata.serialize_metadata"></a>
#### serialize`_`metadata

```python
serialize_metadata(package_hash: str, package_id: PackageId, description: str, nft_image_hash: str) -> str
```

Serialize metadata.

<a name="autonomy.chain.metadata.publish_metadata"></a>
#### publish`_`metadata

```python
publish_metadata(package_id: PackageId, package_path: Path, nft: NFTHashOrPath, description: str) -> Tuple[str, str]
```

Publish service metadata.

