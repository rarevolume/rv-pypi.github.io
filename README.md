# rv-pypi.github.io
Package server for private repos

## Installing a package

To install a module served here, you must pass the `--extra-index-url` flag along with the public url:

    pip install rv_transcode --extra-index-url https://rarevolume.github.io/rv-pypi.github.io/

This will install the latest version of the library.

To install a specific version, specify like so

    pip install rv_transcode==0.0.18 --extra-index-url https://rarevolume.github.io/rv-pypi.github.io/

## Publishing a release

To add a release to the index, open the index.html for the project and add a link pointing to the github link containing the commit hash for the version or the link the the published release if you've done so.

    <a href="git+https://github.com/rarevolume/rv_transcode@e1cbc0ce868879c7895a19b77fce074350efc04d#egg=rv_transcode-0.0.18" data-requires-python=">=3.8.0">rv_transcode-0.0.18</a>

Note: The version number must match up with the version number within the package's setup.py file or pip may fail.

## Specify a package in requirements.txt

After installed, you can do `pip freeze > requirments.txt`, which will have the package name and version, but does not include this url, so you must add `--extra-index-url https://rarevolume.github.io/rv-pypi.github.io/` above where the package is specified manually.

    --extra-index-url https://rarevolume.github.io/rv-pypi.github.io/
    rv-transcode==0.0.17

Optionally, you can copy `pip_freeze.py` to be adjacent to your env folder to append the necessary lines automatically.
