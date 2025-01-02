<a name="autonomy.cli.helpers.image"></a>
# autonomy.cli.helpers.image

Image helpers.

<a name="autonomy.cli.helpers.image.build_image"></a>
#### build`_`image

```python
build_image(agent: Optional[PublicId], service_dir: Optional[Path], pull: bool = False, version: Optional[str] = None, image_author: Optional[str] = None, extra_dependencies: Optional[Tuple[Dependency, ...]] = None, dockerfile: Optional[Path] = None) -> None
```

Build agent/service image.

